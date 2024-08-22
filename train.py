
#train

# import random
# import json
# import pickle
# import numpy as np
# import nltk
# from nltk.stem import WordNetLemmatizer
# import tensorflow as tf

# lemmatizer = WordNetLemmatizer()

# # Load intents file
# intents = json.loads(open("C:\\food\\myenv\\intents.json").read())

# words = []
# classes = []
# documents = []
# ignore_letters = ['?', '!', '.', ',']

# # Process each intent in the intents file
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         word_list = nltk.word_tokenize(pattern)
#         words.extend(word_list)
#         documents.append((word_list, intent['tag']))
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

# # Lemmatize and sort words
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
# words = sorted(set(words))

# # Sort classes
# classes = sorted(set(classes))

# # Save words and classes
# pickle.dump(words, open('words.pkl', 'wb'))
# pickle.dump(classes, open('classes.pkl', 'wb'))

# # Prepare training data
# training = []
# output_empty = [0] * len(classes)

# for doc in documents:
#     bag = []
#     word_patterns = doc[0]
#     word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
#     for word in words:
#         bag.append(1) if word in word_patterns else bag.append(0)

#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append(bag + output_row)

# random.shuffle(training)
# training = np.array(training)

# # Create train and test lists
# train_x = training[:, :len(words)]
# train_y = training[:, len(words):]

# # Create model
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(64, activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))

# sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_food.h5', hist)
# print("Training complete and model saved!")









#added welcome message

# import random
# import json
# import pickle
# import numpy as np
# import nltk
# from nltk.stem import WordNetLemmatizer
# import tensorflow as tf

# lemmatizer = WordNetLemmatizer()

# # Load intents file
# intents = json.loads(open("C:\\food\\myenv\\intents.json").read())

# words = []
# classes = []
# documents = []
# ignore_letters = ['?', '!', '.', ',']

# # Process each intent in the intents file
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         word_list = nltk.word_tokenize(pattern)
#         words.extend(word_list)
#         documents.append((word_list, intent['tag']))
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

# # Lemmatize and sort words
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
# words = sorted(set(words))

# # Sort classes
# classes = sorted(set(classes))

# # Save words and classes
# pickle.dump(words, open('words.pkl', 'wb'))
# pickle.dump(classes, open('classes.pkl', 'wb'))

# # Prepare training data
# training = []
# output_empty = [0] * len(classes)

# for doc in documents:
#     bag = []
#     word_patterns = doc[0]
#     word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
#     for word in words:
#         bag.append(1) if word in word_patterns else bag.append(0)

#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append(bag + output_row)

# random.shuffle(training)
# training = np.array(training)

# # Create train and test lists
# train_x = training[:, :len(words)]
# train_y = training[:, len(words):]

# # Create model
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(64, activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))

# sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_food.h5', hist)
# print("Training complete and model saved!")









#added add to cart

# import random
# import json
# import pickle
# import numpy as np
# import nltk
# from nltk.stem import WordNetLemmatizer
# import tensorflow as tf

# lemmatizer = WordNetLemmatizer()

# # Load intents file
# intents = json.loads(open("C:\\food\\myenv\\intents.json").read())

# words = []
# classes = []
# documents = []
# ignore_letters = ['?', '!', '.', ',']

# # Process each intent in the intents file
# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         word_list = nltk.word_tokenize(pattern)
#         words.extend(word_list)
#         documents.append((word_list, intent['tag']))
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

# # Lemmatize and sort words
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
# words = sorted(set(words))

# # Sort classes
# classes = sorted(set(classes))

# # Save words and classes
# pickle.dump(words, open('words.pkl', 'wb'))
# pickle.dump(classes, open('classes.pkl', 'wb'))

# # Prepare training data
# training = []
# output_empty = [0] * len(classes)

# for doc in documents:
#     bag = []
#     word_patterns = doc[0]
#     word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
#     for word in words:
#         bag.append(1) if word in word_patterns else bag.append(0)

#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append(bag + output_row)

# random.shuffle(training)
# training = np.array(training)

# # Create train and test lists
# train_x = training[:, :len(words)]
# train_y = training[:, len(words):]

# # Create model
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(64, activation='relu'))
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))

# sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_food.h5', hist)
# print("Training complete and model saved!")







#only message not cart

import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf

lemmatizer = WordNetLemmatizer()

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')



# Load intents file
intents = json.loads(open("C:\\food\\myenv\\intents.json").read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

# Process each intent in the intents file
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and sort words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(set(words))

# Sort classes
classes = sorted(set(classes))

# Save words and classes
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Prepare training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append(bag + output_row)

random.shuffle(training)
training = np.array(training)

# Create train and test lists
train_x = training[:, :len(words)]
train_y = training[:, len(words):]

# Create model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_food.h5', hist)
print("Training complete and model saved!")

