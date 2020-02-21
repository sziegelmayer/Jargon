def heatmap(df):
    corr = df.corr(method="spearman")
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(10,10),dpi=300)
        ax.tick_params(axis='both', which='both', labelsize=14)
        ax = sns.heatmap(corr, mask=mask, square=True, cmap="viridis")
