from flower_predictor import app

if __name__ == '__main__':

    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(debug=True)