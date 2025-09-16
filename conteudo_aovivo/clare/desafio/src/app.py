import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
import joblib

df = pd.read_csv('data/raw/imdb.csv')

if 'Runtime' in df.columns:
    df['Runtime'] = df['Runtime'].astype(str).str.replace('min', '', regex=False).str.strip()
    df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')

if 'Gross' in df.columns:
    df['Gross'] = df['Gross'].astype(str).str.replace(',', '', regex=False).str.strip()
    df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

if 'Released_Year' in df.columns:
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce').astype('Int64')

df.to_csv('data/processed/desafio_formatado.csv', index=False)

print(df.info())
print(df.head(10))

media = df['IMDB_Rating'].mean()
mediana = df['IMDB_Rating'].median()
moda = df['IMDB_Rating'].mode()[0]
print(f"Média da nota IMDB: {media:.2f}")
print(f"Mediana da nota IMDB: {mediana:.2f}")
print(f"Moda da nota IMDB: {moda:.2f}")

minimo = df['IMDB_Rating'].min()
maximo = df['IMDB_Rating'].max()
desvio = df['IMDB_Rating'].std()
print(f"Mínimo da nota IMDB: {minimo:.2f}")
print(f"Máximo da nota IMDB: {maximo:.2f}")
print(f"Desvio padrão da nota IMDB: {desvio:.2f}")


plt.hist(df['IMDB_Rating'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Média ({media:.2f})')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1.5, label=f'Mediana ({mediana:.2f})')
plt.axvline(moda, color='orange', linestyle='dashed', linewidth=1.5, label=f'Moda ({moda:.2f})')
plt.title('Histograma da Nota IMDB')
plt.xlabel('Nota IMDB')
plt.ylabel('Frequência')
plt.legend()
plt.show()

plt.boxplot(df['IMDB_Rating'].dropna(), vert=False)
plt.title('Boxplot da Nota IMDB')
plt.xlabel('Nota IMDB')
plt.show()

notas = df['IMDB_Rating'].dropna()

Q1 = notas.quantile(0.25)
Q2 = notas.quantile(0.50)  # mediana
Q3 = notas.quantile(0.75)
IQR = Q3 - Q1

lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers_df = df[(df['IMDB_Rating'] < lim_inf) | (df['IMDB_Rating'] > lim_sup)][['Series_Title', 'IMDB_Rating']]

outliers_df = outliers_df.sort_values('IMDB_Rating', ascending=False)
if len(outliers_df) > 25:
    outliers_df = outliers_df.head(25)

print("\n==== Quartis e Limiares (IMDB_Rating) ====")
print(f"Q1: {Q1:.2f} | Q2 (mediana): {Q2:.2f} | Q3: {Q3:.2f} | IQR: {IQR:.2f}")
print(f"Limite inferior: {lim_inf:.2f} | Limite superior: {lim_sup:.2f}")
print(f"Total de outliers: {len(outliers_df)}")

if not outliers_df.empty:
    plt.figure()
    valid_indices = df['IMDB_Rating'].dropna().index
    valid_ratings = df.loc[valid_indices, 'IMDB_Rating']
    plt.scatter(valid_indices, valid_ratings, color='lightgray', label='Filmes')
    outlier_indices = outliers_df.index
    outlier_ratings = outliers_df['IMDB_Rating']
    plt.scatter(outlier_indices, outlier_ratings, color='red', label='Outliers')
    plt.title('Distribuição da Nota IMDB com Outliers Destacados')
    plt.xlabel('Índice do Filme no DataFrame')
    plt.ylabel('Nota IMDB')
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print('Não foram encontrados outliers na distribuição da nota IMDB com a regra de 1.5*IQR.')

if 'Genre' in df.columns:
    genres_exploded = df.assign(Genre=df['Genre'].astype(str).str.split(',')).explode('Genre')
    genres_exploded['Genre'] = genres_exploded['Genre'].str.strip()

    genres_exploded = genres_exploded.dropna(subset=['Genre', 'IMDB_Rating'])

    genero_stats = (
        genres_exploded
        .groupby('Genre')['IMDB_Rating']
        .agg(media='mean', mediana='median', qtd='count')
        .reset_index()
        .sort_values('media', ascending=False)
    )

    print("\n==== Estatísticas por Gênero (IMDB_Rating) ====")
    print(genero_stats.head(20))

    top10 = genero_stats.head(10)
    plt.figure()
    plt.bar(top10['Genre'], top10['media'])
    plt.xticks(rotation=45, ha='right')
    plt.title('Média da Nota IMDB por Gênero (Top 10)')
    plt.xlabel('Gênero')
    plt.ylabel('Média da Nota IMDB')
    plt.tight_layout()
    plt.show()

    sort_cols = ['Genre', 'IMDB_Rating']
    sort_asc = [True, False]
    if 'No_of_Votes' in genres_exploded.columns:
        sort_cols.append('No_of_Votes')
        sort_asc.append(False)

    ranked = genres_exploded.sort_values(sort_cols, ascending=sort_asc, na_position='last')

    cols_desejadas = ['Genre', 'Series_Title', 'IMDB_Rating', 'No_of_Votes', 'Meta_score', 'Released_Year', 'Director']
    cols_existentes = [c for c in cols_desejadas if c in ranked.columns]
    top10_por_genero = ranked.groupby('Genre', group_keys=False).head(10)[cols_existentes]

    top10_por_genero.to_csv('data/processed/top10_por_genero.csv', index=False)
    print("\n==== Top 10 por Gênero (IMDB_Rating) ====")
    print(top10_por_genero.head(30))
    print("\nArquivo salvo: top10_por_genero.csv")
else:
    print('\nColuna "Genre" não encontrada no DataFrame.')

if 'Gross' in df.columns and 'IMDB_Rating' in df.columns:
    cols_util = ['Series_Title', 'IMDB_Rating', 'Gross', 'No_of_Votes', 'Meta_score', 'Released_Year', 'Genre', 'Director']
    cols_util = [c for c in cols_util if c in df.columns]

    top20_gross = (
        df.dropna(subset=['Gross'])
          .sort_values('Gross', ascending=False)
          .head(20)[cols_util]
          .copy()
    )

    _notas = df['IMDB_Rating'].dropna()
    Q1_global = _notas.quantile(0.25)
    Q3_global = _notas.quantile(0.75)

    def cat_avaliacao(x):
        if pd.isna(x):
            return 'Sem nota'
        if x >= Q3_global:
            return 'Alta (>= Q3)'
        if x <= Q1_global:
            return 'Baixa (<= Q1)'
        return 'Média'

    top20_gross['Categoria_Avaliacao'] = top20_gross['IMDB_Rating'].apply(cat_avaliacao)

    top20_gross.to_csv('data/processed/top20_gross_com_avaliacao.csv', index=False)
    print("\n==== Top 20 por Arrecadação (com categoria de avaliação) ====")
    print(top20_gross)
    print("\nArquivo salvo: top20_gross_com_avaliacao.csv")

    try:
        cores = top20_gross['Categoria_Avaliacao'].map({
            'Alta (>= Q3)': 'green',
            'Média': 'gray',
            'Baixa (<= Q1)': 'red',
            'Sem nota': 'lightgray'
        })
        plt.figure()
        plt.scatter(top20_gross['Gross'], top20_gross['IMDB_Rating'], c=cores)
        from matplotlib.ticker import FuncFormatter, MaxNLocator

        def _human_fmt(x, pos):
            try:
                x = float(x)
            except Exception:
                return str(x)
            if abs(x) >= 1_000_000_000:
                return f"{x/1_000_000_000:.1f}B"
            if abs(x) >= 1_000_000:
                return f"{x/1_000_000:.1f}M"
            if abs(x) >= 1_000:
                return f"{x/1_000:.0f}K"
            return f"{x:.0f}"

        ax = plt.gca()
        ax.xaxis.set_major_formatter(FuncFormatter(_human_fmt))
        ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        plt.grid(alpha=0.3, linestyle='--', axis='both')

        rotular = set()
        rotular.update(top20_gross.nlargest(8, 'Gross').index.tolist())
        if 'IMDB_Rating' in top20_gross.columns:
            rotular.update(top20_gross.nlargest(2, 'IMDB_Rating').index.tolist())
            rotular.update(top20_gross.nsmallest(2, 'IMDB_Rating').index.tolist())

        for i, row in top20_gross.iterrows():
            if i in rotular:
                plt.annotate(str(row['Series_Title'])[:22],
                             (row['Gross'], row['IMDB_Rating']),
                             fontsize=8, xytext=(4, 4), textcoords='offset points')
        plt.title('Top 20 por Arrecadação: Gross x IMDB_Rating')
        plt.xlabel('Arrecadação (Gross)')
        plt.ylabel('IMDB_Rating')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Falha ao plotar scatter de Top 20 Gross: {e}")
else:
    print('\nColunas necessárias para análise de arrecadação não encontradas (Gross/IMDB_Rating).')

try:
    import numpy as np
    possiveis = ['IMDB_Rating', 'Gross', 'No_of_Votes', 'Meta_score', 'Runtime', 'Released_Year']
    num_exist = [c for c in possiveis if c in df.columns]
    corr = df[num_exist].corr(numeric_only=True)
    if not corr.empty:
        fig, ax = plt.subplots()
        im = ax.imshow(corr.values, cmap='viridis')
        ax.set_xticks(range(len(num_exist)))
        ax.set_yticks(range(len(num_exist)))
        ax.set_xticklabels(num_exist, rotation=45, ha='right')
        ax.set_yticklabels(num_exist)
        for i in range(len(num_exist)):
            for j in range(len(num_exist)):
                ax.text(j, i, f"{corr.values[i, j]:.2f}", ha='center', va='center', fontsize=8, color='white' if abs(corr.values[i, j])>0.5 else 'black')
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        ax.set_title('Correlação entre variáveis numéricas')
        fig.tight_layout()
        plt.show()
    else:
        print('\nSem colunas numéricas suficientes para correlação.')
except Exception as e:
    print(f'Falha ao gerar heatmap de correlação: {e}')

try:
    if {'Gross', 'IMDB_Rating'}.issubset(df.columns):
        valid_xy = df[['Gross', 'IMDB_Rating', 'Series_Title']].dropna()
        if not valid_xy.empty:
            x_med = valid_xy['Gross'].median()
            y_med = valid_xy['IMDB_Rating'].median()

            plt.figure()
            plt.scatter(valid_xy['Gross'], valid_xy['IMDB_Rating'], s=15, alpha=0.6, color='lightgray')
            plt.axvline(x_med, color='black', linestyle='--', linewidth=1)
            plt.axhline(y_med, color='black', linestyle='--', linewidth=1)

            from matplotlib.ticker import FuncFormatter, MaxNLocator
            def _human_fmt(x, pos):
                try:
                    x = float(x)
                except Exception:
                    return str(x)
                if abs(x) >= 1_000_000_000:
                    return f"{x/1_000_000_000:.1f}B"
                if abs(x) >= 1_000_000:
                    return f"{x/1_000_000:.1f}M"
                if abs(x) >= 1_000:
                    return f"{x/1_000:.0f}K"
                return f"{x:.0f}"
            ax = plt.gca()
            ax.xaxis.set_major_formatter(FuncFormatter(_human_fmt))
            ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
            plt.grid(alpha=0.3, linestyle='--', axis='both')

            plt.title('Quadrantes: Arrecadação (Gross) × Nota IMDB (medianas)')
            plt.xlabel('Arrecadação (Gross)')
            plt.ylabel('IMDB_Rating')
            plt.tight_layout()
            plt.show()
        else:
            print('Sem dados válidos para quadrantes de Gross x IMDB_Rating.')
    else:
        print('Colunas Gross/IMDB_Rating ausentes para quadrantes.')
except Exception as e:
    print(f'Falha ao gerar quadrantes Gross × IMDB_Rating: {e}')

def recommend_by_genre(df_base, genero, k=5, min_votes=10000):
    if 'Genre' not in df_base.columns or 'IMDB_Rating' not in df_base.columns:
        print('Campos necessários ausentes (Genre/IMDB_Rating).')
        return pd.DataFrame()
    tmp = df_base.copy()
    tmp['Genre'] = tmp['Genre'].astype(str)
    tmp = tmp.assign(Genre=tmp['Genre'].str.split(',')).explode('Genre')
    tmp['Genre'] = tmp['Genre'].str.strip().str.lower()
    genero_norm = str(genero).strip().lower()
    tmp = tmp[tmp['Genre'] == genero_norm]
    tmp = tmp.dropna(subset=['IMDB_Rating'])
    if 'No_of_Votes' in tmp.columns and min_votes is not None:
        tmp = tmp[tmp['No_of_Votes'].fillna(0) >= min_votes]
    sort_cols = ['IMDB_Rating'] + (['No_of_Votes'] if 'No_of_Votes' in tmp.columns else [])
    sort_asc = [False] + ([False] if 'No_of_Votes' in tmp.columns else [])
    tmp = tmp.sort_values(sort_cols, ascending=sort_asc)
    cols_final = [c for c in ['Series_Title', 'Genre', 'IMDB_Rating', 'No_of_Votes', 'Meta_score', 'Released_Year', 'Director'] if c in tmp.columns]
    recs = tmp.head(k)[cols_final]
    if not recs.empty:
        fname = f"recs_{genero_norm}_top{k}.csv"
        recs.to_csv(f"data/processed/{fname}", index=False)
        print(f"\nRecomendações por gênero ('{genero_norm}') salvas em: data/processed/{fname}")
        print(recs)
    else:
        print(f"\nSem recomendações para o gênero '{genero}'.")
    return recs

try:
    recommend_by_genre(df, genero='Drama', k=5, min_votes=20000)
except Exception as e:
    print(f'Falha na recomendação por gênero: {e}')

try:
    numeric_candidates = ['Gross', 'No_of_Votes', 'Runtime', 'Meta_score', 'Released_Year']
    numeric_cols = [c for c in numeric_candidates if c in df.columns]
    categorical_cols = [c for c in ['Certificate'] if c in df.columns]
    text_col = 'Overview' if 'Overview' in df.columns else None

    feature_cols = numeric_cols + categorical_cols + ([text_col] if text_col else [])
    if len(feature_cols) == 0:
        print('\n[Modelo] Nenhuma feature disponível. Pulei o treinamento.')
    else:
        data_model = df.dropna(subset=['IMDB_Rating']).copy()
        if text_col and text_col in data_model.columns:
            data_model[text_col] = data_model[text_col].fillna('')
        X = data_model[feature_cols]
        y = data_model['IMDB_Rating']

        transformers = []
        if numeric_cols:
            num_pipe = Pipeline([
                ('imp', SimpleImputer(strategy='median')),
                ('sc', StandardScaler(with_mean=False))
            ])
            transformers.append(('num', num_pipe, numeric_cols))
        if categorical_cols:
            cat_pipe = Pipeline([
                ('imp', SimpleImputer(strategy='most_frequent')),
                ('oh', OneHotEncoder(handle_unknown='ignore'))
            ])
            transformers.append(('cat', cat_pipe, categorical_cols))
        if text_col:
            transformers.append(('txt', TfidfVectorizer(max_features=5000, stop_words='english'), text_col))

        preprocess = ColumnTransformer(transformers, remainder='drop')
        ridge = Ridge(alpha=1.0)
        model_pipeline = Pipeline(steps=[('prep', preprocess), ('model', ridge)])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model_pipeline.fit(X_train, y_train)

        y_pred = model_pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        print("\n==== Modelo Ridge (baseline) ====")
        print(f"MAE: {mae:.3f} | RMSE: {rmse:.3f} | R²: {r2:.3f}")

        os.makedirs('models', exist_ok=True)
        joblib.dump(model_pipeline, 'models/model.pkl')
        print("Modelo salvo em: models/model.pkl")
except Exception as e:
    print(f"Falha no treinamento/salvamento do modelo: {e}")

def predict_shawshank(trained_pipeline, df_base):
    """Prevê a nota do IMDB para 'The Shawshank Redemption' usando o pipeline treinado."""
    try:
        if trained_pipeline is None:
            print('Pipeline não treinado/carregado.')
            return None

        numeric_candidates = ['Gross', 'No_of_Votes', 'Runtime', 'Meta_score', 'Released_Year']
        numeric_cols = [c for c in numeric_candidates if c in df_base.columns]
        categorical_cols = [c for c in ['Certificate'] if c in df_base.columns]
        text_col = 'Overview' if 'Overview' in df_base.columns else None
        feature_cols = numeric_cols + categorical_cols + ([text_col] if text_col else [])
        if len(feature_cols) == 0:
            print('[Shawshank] Sem features disponíveis para previsão.')
            return None

        title = 'The Shawshank Redemption'
        if 'Series_Title' not in df_base.columns:
            print(f"[Shawshank] Coluna 'Series_Title' ausente.")
            return None
        mask = df_base['Series_Title'].astype(str).str.lower().str.contains('shawshank')
        if not mask.any():
            print(f"[Shawshank] Filme contendo 'Shawshank' não encontrado no DataFrame.")
            return None
        row = df_base[mask].iloc[0]
        if text_col and text_col in df_base.columns:
            row[text_col] = '' if pd.isna(row[text_col]) else row[text_col]
        X_one = pd.DataFrame([row[feature_cols]], columns=feature_cols)
        pred = trained_pipeline.predict(X_one)[0]
        print(f"\nPrevisão para '{title}': {pred:.2f}")
        return float(pred)
    except Exception as e:
        print(f"Falha na previsão de Shawshank: {e}")
        return None

def predict_by_title(trained_pipeline, df_base, title_substr):
    """Prevê a nota do IMDB para o primeiro filme cujo título contém 'title_substr' (case-insensitive)."""
    try:
        if trained_pipeline is None:
            print('Pipeline não treinado/carregado.')
            return None
        if 'Series_Title' not in df_base.columns:
            print("[predict_by_title] Coluna 'Series_Title' ausente.")
            return None

        numeric_candidates = ['Gross', 'No_of_Votes', 'Runtime', 'Meta_score', 'Released_Year']
        numeric_cols = [c for c in numeric_candidates if c in df_base.columns]
        categorical_cols = [c for c in ['Certificate'] if c in df_base.columns]
        text_col = 'Overview' if 'Overview' in df_base.columns else None
        feature_cols = numeric_cols + categorical_cols + ([text_col] if text_col else [])
        if len(feature_cols) == 0:
            print('[predict_by_title] Sem features disponíveis para previsão.')
            return None

        sub = str(title_substr).strip().lower()
        mask = df_base['Series_Title'].astype(str).str.lower().str.contains(sub)
        if not mask.any():
            print(f"[predict_by_title] Nenhum título contendo '{title_substr}' encontrado.")
            return None
        row = df_base[mask].iloc[0]
        if text_col and text_col in df_base.columns:
            row[text_col] = '' if pd.isna(row[text_col]) else row[text_col]
        X_one = pd.DataFrame([row[feature_cols]], columns=feature_cols)
        pred = trained_pipeline.predict(X_one)[0]
        print(f"Previsão para título contendo '{title_substr}': {float(pred):.2f} → {row['Series_Title']}")
        return float(pred)
    except Exception as e:
        print(f"Falha no predict_by_title('{title_substr}'): {e}")
        return None

try:
    _ = predict_shawshank(model_pipeline if 'model_pipeline' in globals() else None, df)
except Exception as e:
    print(f'Erro ao executar previsão de Shawshank: {e}')

def recommend_by_genre_scored(df_base, genero, k=5, min_votes=10000):
    if 'Genre' not in df_base.columns or 'IMDB_Rating' not in df_base.columns:
        print('Campos necessários ausentes (Genre/IMDB_Rating).')
        return pd.DataFrame()
    tmp = df_base.copy()
    tmp['Genre'] = tmp['Genre'].astype(str)
    tmp = tmp.assign(Genre=tmp['Genre'].str.split(',')).explode('Genre')
    tmp['Genre'] = tmp['Genre'].str.strip().str.lower()
    genero_norm = str(genero).strip().lower()
    tmp = tmp[tmp['Genre'] == genero_norm]
    tmp = tmp.dropna(subset=['IMDB_Rating'])
    if 'No_of_Votes' in tmp.columns:
        tmp['No_of_Votes'] = tmp['No_of_Votes'].fillna(0)
    else:
        tmp['No_of_Votes'] = 0
    if min_votes is not None:
        tmp = tmp[tmp['No_of_Votes'] >= min_votes]
    tmp['score'] = tmp['IMDB_Rating'] * np.log10(tmp['No_of_Votes'] + 1)
    tmp = tmp.sort_values(['score', 'IMDB_Rating', 'No_of_Votes'], ascending=[False, False, False])
    cols_final = [c for c in ['Series_Title', 'Genre', 'IMDB_Rating', 'No_of_Votes', 'score', 'Meta_score', 'Released_Year', 'Director'] if c in tmp.columns]
    recs = tmp.head(k)[cols_final]
    if not recs.empty:
        fname = f"recs_{genero_norm}_score_top{k}.csv"
        recs.to_csv(f"data/processed/{fname}", index=False)
        print(f"\nRecomendações por gênero com score ('{genero_norm}') salvas em: data/processed/{fname}")
        print(recs)
    else:
        print(f"\nSem recomendações (score) para o gênero '{genero}'.")
    return recs

try:
    recommend_by_genre_scored(df, genero='Drama', k=5, min_votes=20000)
except Exception as e:
    print(f'Falha na recomendação por gênero (score): {e}')