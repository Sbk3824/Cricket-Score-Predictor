<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Score Details</title>

    <!-- Bootstrap core CSS -->
    <link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="{{ url_for('static', filename='css/sign.css') }}" rel="stylesheet">

    <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </head>

  <body>

    <div class="container">
      <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" ><a href="{{ url_for('index') }}">Home</a>
                    </li>
                    <li role="presentation" class="active"><a href="#">Score Predictor</a>
                    </li>
                    <li role="presentation"><a href="results">Results</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Cricket Score Predictor</h3>
        </div>
      <br>
      <br>
      
      <form class="form" method="post" action="/process">
        <h3 class="form-signin-heading">Enter the Match Details</h3>
        <div class="form-row">
        <div class="form-group col-md-6">
          <label for="inputName">Runs Scored</label>
          <input type="text" id="inputName" name="name" class="form-control" placeholder="Runs" required autofocus>
        </div>
        <div class="form-group col-md-6">
          <label for="comment" >Balls</label>
            <input type="text" class="form-control" name="comment" id="comment" placeholder="Balls" required>
        </div>
      </div>
        <div class="form-row">
        <div class="form-group col-md-6">
          <label for="wickets" >Wickets</label>
          <input type="text" id="wickets" name="wickets" class="form-control" placeholder="Wickets" required autofocus>
        </div>
        <div class="form-group col-md-6">
          <label for="ga" >Venue</label>
	<select class="form-control" id="exampleFormControlSelect1">
		<option value="">Select</option>
     		<option value="177">Civil Service Cricket Club, Stormont, Belfast - Ireland</option>
      		<option value="232">Lord's, London - England</option>
      		<option value="247">Kennington Oval, London - England</option>
      		<option value="214">Riverside Ground, Chester-le-Street - England</option>
      		<option value="210">Grange Cricket Club, Raeburn Place, Edinburgh - Scotland</option>
      		<option value="206">Old Trafford, Manchester - England</option>
      		<option value="285">Headingley, Leeds - England</option>
      		<option value="225">VRA Ground, Amstelveen - Netherlands</option>
      		<option value="214">Harare Sports Club - Zimbabwe</option>
      		<option value="163">Cambusdoon New Ground, Ayr - Scotland</option>
      		<option value="189">Toronto Cricket, Skating and Curling Club - Canada</option>
      		<option value="193">Gymkhana Club Ground, Nairobi - Kenya</option>
      		<option value="167">Sinhalese Sports Club Ground, Colombo - Sri Lanka</option>
      		<option value="204">Sophia Gardens, Cardiff - England</option>
      		<option value="258">The Rose Bowl, Southampton - England</option>
      		<option value="229">Trent Bridge, Nottingham - England</option>
      		<option value="207">Edgbaston, Birmingham - England</option>
      		<option value="204">Kinrara Academy Oval, Kuala Lumpur - Malaysia</option>
      		<option value="262">Mangaung Oval, Bloemfontein - South Africa</option>
      		<option value="195">Buffalo Park, East London - South Africa</option>
      		<option value="246">Senwes Park, Potchefstroom - South Africa</option>
      		<option value="261">Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh - India</option>
      		<option value="224">Sardar Patel (Gujarat) Stadium, Motera, Ahmedabad - India</option>
      		<option value="235">Sawai Mansingh Stadium, Jaipur - India</option>
      		<option value="150">Brabourne Stadium, Mumbai - India</option>
      		<option value="224">Mombasa Sports Club Ground - Kenya</option>
      		<option value="245">Kingsmead, Durban - South Africa</option>
      		<option value="243">Newlands, Cape Town - South Africa</option>
      		<option value="217">St George's Park, Port Elizabeth - South Africa</option>
      		<option value="199">Sheikh Abu Naser Stadium, Khulna - Bangladesh</option>
      		<option value="219">Willowmoore Park, Benoni - South Africa</option>      		
       </select>
        </div>
        </div>
        <div class="form-row">
        <div class="form-group col-md-6">
          <label for="ppballs">PP Balls</label>
            <input type="text" class="form-control" name="ppballs" id="ppballs" placeholder="Power Play Balls" required>
        </div>
        <div class="form-group col-md-6">
          <label for="overs" >Overs</label>
          <input type="text" id="overs" name="overs" class="form-control" placeholder="Overs" required autofocus>
        </div>
        </div>

        <button class="btn btn-lg btn-primary btn-block" type="submit">Compare Results</button>
      </form>
<br>
<br>


<div class="container">
  <!-- Trigger the modal with a button -->
  <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">Results</button>

  <!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Predicted Scores</h4>
        </div>
        <div class="modal-body">
          <p> Actual Score: {{ actual_Score }}</p>
          <p> DLS Score: {{ DL_Score }}</p>
          <p> Improvised DLS Score: {{ Ml_Score }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
      
    </div>
  </div>
  
</div>

<div class="container">

  <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">Model Performance</button>

  <!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Predicted Scores</h4>
        </div>
        <div class="modal-body">
          <p> Actual Score: {{ actual_Score }}</p>
          <p> DLS Score: {{ DL_Score }}</p>
          <p> Improvised DLS Score: {{ Ml_Score }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
      
    </div>
  </div>

</div>



      
</div> <!-- /container -->
</body>
</html>
