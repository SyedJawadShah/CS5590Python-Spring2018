import cnn_model

histories = []

for i in range(RUNS):
    print('Running iteration %i/%i' % (i + 1, RUNS))

    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=VAL_SIZE, random_state=42)

    emb_layer = None
    if USE_GLOVE:
        emb_layer = create_glove_embeddings()

    model = cnn_model.build_cnn(
        embedding_layer=emb_layer,
        num_words=MAX_NUM_WORDS,
        embedding_dim=EMBEDDING_DIM,
        filter_sizes=FILTER_SIZES,
        feature_maps=FEATURE_MAPS,
        max_seq_length=MAX_SEQ_LENGTH,
        dropout_rate=DROPOUT_RATE
    )

    model.compile(
        loss='binary_crossentropy',
        optimizer=Adadelta(clipvalue=3),
        metrics=['accuracy']
    )

    history = model.fit(
        X_train, y_train,
        epochs=NB_EPOCHS,
        batch_size=BATCH_SIZE,
        verbose=1,
        validation_data=(X_val, y_val),
        callbacks=[ModelCheckpoint('model-%i.h5' % (i + 1), monitor='val_loss',
                                   verbose=1, save_best_only=True, mode='min'),
                   ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=4, min_lr=0.01)
                   ]
    )
    print()
    histories.append(history.history)

    with open('history.pkl', 'wb') as f:
        pickle.dump(histories, f)

    histories = pickle.load(open('history.pkl', 'rb'))


    def get_avg(histories, his_key):
        tmp = []
        for history in histories:
            tmp.append(history[his_key][np.argmin(history['val_loss'])])
        return np.mean(tmp)


    print('Training: \t%0.4f loss / %0.4f acc' % (get_avg(histories, 'loss'),
                                                  get_avg(histories, 'acc')))
    print('Validation: \t%0.4f loss / %0.4f acc' % (get_avg(histories, 'val_loss'),
                                                    get_avg(histories, 'val_acc')))
    X_test = negative_docs_test + positive_docs_test
    y_test = [0 for _ in range(len(negative_docs_test))] + [1 for _ in range(len(positive_docs_test))]

    sequences_test = tokenizer.texts_to_sequences(X_test)

    X_test = pad_sequences(sequences_test, maxlen=MAX_SEQ_LENGTH, padding='post')

    test_loss = []
    test_accs = []

    for i in range(0, RUNS):
        cnn_ = load_model("model-%i.h5" % (i + 1))

        score = cnn_.evaluate(X_test, y_test, verbose=1)
        test_loss.append(score[0])
        test_accs.append(score[1])

        print('Running test with model %i: %0.4f loss / %0.4f acc' % (i + 1, score[0], score[1]))

    print('\nAverage loss / accuracy on testset: %0.4f loss / %0.4f acc' % (np.mean(test_loss),
                                                                            np.mean(test_accs)))
    print('Standard deviation: (+-%0.4f) loss / (+-%0.4f) acc' % (np.std(test_loss), np.std(test_accs)))