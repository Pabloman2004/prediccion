

print("Que quieres predecir?\n\n")

x = input("1. Resultado partido \n2. Resultado de la liga \n3.remates a puerta de un jugador\n\n")

if x == "1":
    import predict_match
    predict_match.PredictMatch().load_data()

