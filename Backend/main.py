from Config.Server import app

if __name__ == '__main__':
    print('Iniciando Servidor')
    app.run(host='0.0.0.0', port=5000, debug=True)

