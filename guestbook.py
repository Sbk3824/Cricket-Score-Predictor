from flask import Flask, render_template, request
from evaluation import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')


@app.route('/predictor')
def predictor():
	return render_template('predictor.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	wickets = request.form['wickets']
	ga = request.form['ga']
	ppballs = request.form['ppballs']
	overs = request.form['overs']

	score = [name,comment,wickets,ga,ppballs,overs]
	print score
	col = pd.DataFrame([score],columns=['runs','balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs'])
	print col
	#col.index = ['runs','balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']
	col_copy =  col[['balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']]
	print col_copy
	predicted = predictor_score(col_copy)
	predicted_scores = np.array(predicted)
	predicted_scores = np.reshape(predicted_scores, (np.shape(predicted_scores)[0], 1L))
	print 'Reshape', predicted_scores
	col_df= pd.DataFrame(col[['runs']].as_matrix())
	print col_df

	algo ={}
	result = {}

	for i in range(len(predicted_scores)):
		print i
		col_df['ML Predicted'] = predicted_scores[i]
		algo[i] = predicted_scores[i]
		col_df["DL Predicted"] = duckworth_lewis(col)
		print col_df
		result[i] = rmse(col_df.as_matrix())
	

	print result
	min_rmse = min(result,key=lambda x:result[x])
	min_value = algo[min_rmse]
	print 'Minimum RMSE', min_value
	print 'Score1',algo[0]
	actual_Score = col_df[0][0]
	print actual_Score
	Ml_Score = col_df.iloc[0]['ML Predicted']
	print Ml_Score
	DL_Score = col_df.iloc[0]['DL Predicted']
	print 'DL_Score',DL_Score
	#print result
	

	return render_template('predictor.html', minvalue=min_value, score1=algo[0],score2=algo[1], score3=algo[2], score4=algo[3], score5=algo[4],score6=algo[5], result=result, actual_Score=actual_Score, Ml_Score=Ml_Score, DL_Score=DL_Score)

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)