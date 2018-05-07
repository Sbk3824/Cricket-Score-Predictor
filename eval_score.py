from evaluation import *

def eval_score(data):
	print 'Data',data
	#data.index = ['runs','balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']
	print 'With index',data
	#columns=['runs','balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']
	col = pd.DataFrame([data])
	#col.index = ['runs','balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']
	print 'Col',col
	#col_copy =  col['balls', 'wickets', 'ground_average', 'pp_balls_left', 'total_overs']
	predicted = predictor(col_copy)
	predicted_scores = np.array(predicted)
	predicted_scores = np.reshape(predicted_scores, (np.shape(predicted_scores)[0], 1L))
	col_df = pd.DataFrame(col[['runs']].as_matrix())
	col_df['ML Predicted'] = predicted_scores
	col_df["DL Predicted"] = duckworth_lewis(col)
	print get_rmse(col_df.as_matrix())

#data = [[200,240,6,100,0,50]]
#ml_model(data)
