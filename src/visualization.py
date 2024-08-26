import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def generate_word_count_distribution(df):
    plt.figure(figsize=(8, 4))
    plt.hist(df['word_count'], bins=20, color='#967bb6', alpha=0.7, density=True)
    sns.kdeplot(df['word_count'], color='black', linewidth=2)
    plt.title('Distribution of Review Word Count', fontsize=16)
    plt.xlabel('Word Count', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.xticks(range(0, 700, 50))
    plt.yticks([i/1000 for i in range(0, 15)])
    plt.legend(labels=['KDE', 'Histogram'])
    plt.savefig('./visualization/wordcount.png')
    plt.close()

def generate_sentiment_distribution(df):
    sns.countplot(x='label', data=df, palette='coolwarm')
    plt.title('Preliminary Sentiment Distribution')
    plt.savefig('./visualization/Preliminary_Sentiment_Distribution.png')
    plt.close()

def generate_verified_distribution(df):
    
    verified_counts = df['verified'].value_counts(normalize=True) * 100
    bar_colors = ['#3498db', '#9b59b6']
    plt.bar(verified_counts.index, verified_counts.values, color=bar_colors)
    plt.xlabel('Verification Status')
    plt.ylabel('Percentage')
    plt.title('Distribution of Verified Reviews')
    plt.xticks(verified_counts.index, ['Verified', 'Unverified'])
    plt.savefig('./visualization/Distribution_of_Verified_Reviews.png')
    plt.close()

def generate_most_used_words(df):
    words = " ".join(df['cleaned_reviews']).split()
    stop_words = {'i', 'the', 'would', 'one', 'get', '-'}
    key_words = [word for word in words if word not in stop_words]
    word_counts = Counter(key_words).most_common(20)
    labels, values = zip(*word_counts)
    plt.bar(labels, values)
    plt.xticks(rotation=90)
    plt.title('Most Used Words')
    plt.savefig('./visualization/most_used_words.png')
    plt.close()

def generate_word_clouds(df):
    for sentiment in ['positive', 'negative', 'neutral']:
        subset = df[df['sentiment'] == sentiment]
        text = ' '.join(subset['cleaned_reviews'])
        
        # Skip empty word clouds
        if text.strip():
            wordcloud = WordCloud(width=800, height=400, max_font_size=100, background_color='white').generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title(f'Word Cloud for {sentiment.capitalize()} Sentiment')
            plt.savefig(f'./visualization/Word_Cloud_for_{sentiment.capitalize()}_Sentiment.png')
            plt.close()

def generate_confusion_matrix(y_test, y_pred, model):
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.savefig('./visualization/confusion_matrix.png')
    plt.close()

def generate_vader_sentiment_distribution(df):
    # Calculate label distribution percentages
    label_percentages = df['label'].value_counts(normalize=True) * 100

    # Bar chart
    colors = ['#3498db', '#e74c3c', '#8e44ad']
    labels = ['Positive', 'Negative', 'Neutral']

    plt.bar(labels, label_percentages.reindex([1, -1, 0], fill_value=0), color=colors)
    plt.xlabel('Sentiment Label')
    plt.ylabel('Percentage')
    plt.title('Sentiment Distribution in Customer Reviews')
    plt.ylim(0, 100)

    # Display percentages on the bars
    for i, percentage in enumerate(label_percentages.reindex([1, -1, 0], fill_value=0)):
        plt.text(i, percentage + 2, f"{percentage:.2f}%", ha='center', color='black')

    plt.savefig('./visualization/vader_sentiment_distribution.png')
    plt.close()

def generate_visualizations(df, y_test=None, y_pred=None, model=None):
    generate_word_count_distribution(df)
    generate_sentiment_distribution(df)
    generate_verified_distribution(df)
    generate_most_used_words(df)
    generate_word_clouds(df)
    generate_vader_sentiment_distribution(df)  # Add VADER sentiment distribution
    if y_test is not None and y_pred is not None and model is not None:
        generate_confusion_matrix(y_test, y_pred, model)
