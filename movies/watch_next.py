import spacy

nlp = spacy.load("en_core_web_md")
with open("movies.txt") as movies:
    movie_descriptions = movies.readlines()


def watch_next(description):
    max_similarity = 0
    most_similar_movie = ""
    doc1 = nlp(description)
    for movie_description in movie_descriptions:
        doc2 = nlp(movie_description)
        similarity = doc1.similarity(doc2)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_description.split(":")[0]
    return most_similar_movie.strip()


previous_movie = ("Will he save their world or destroy it? "
                  "When the Hulk becomes too dangerous for the Earth, "
                  "the Illuminati trick Hulk into a shuttle and launch him into space to a "
                  "planet where the Hulk can live in peace. ")

print(watch_next(previous_movie))
