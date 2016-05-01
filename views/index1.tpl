<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SEM SDKS</title>
    <link href='http://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
    <link href="css/bootstrap.css" rel="stylesheet">

    <link href="css/templatestyles.css" rel="stylesheet">
    <link href="css/queries.css" rel="stylesheet">
    <link href="css/animate.css" rel="stylesheet">

      </head>
      <body id="top">
        <header id="home">

          <section class="hero" id="hero">
            <div class="container">
              <div class="row">
                <div class="col-md-12 text-right navicon">
                  <h1 class="animated fadeInDown text-center">SEM<span>SDK'S</span></h1>
                  <p class="animated fadeInUp delay-05s text-center"><span class="bold title_color">S</span>u<span class="bold title_color">D</span>o<span class="bold title_color">K</span>u Solver</p>
                </div>
              </div>
			  <br/><br/>
			  <div class="row animated delay-20s fadeInUp">
              <div class="col-md-12 margin-top-100 ">
              <form role="form" method="post" onsubmit="return false;">
			<a href="./stop" class="confirmation"><button class="btn btn-info btn-fill" type="button"><img style="width:40px" src="../img/newgame.png"/> New Game</button></a>
			<button class="btn btn-info btn-fill" type="submit"><img style="width:40px" src="../img/check.png"/> Check</button>
<div class='row'>

				<div class='col-md-9'>
				    <input readonly style="border:none;background:none;color:#F5F5F5;margin-top:20px;margin-left:280px;" type='text' name='timer' class='timer' />
					<!--<button class='btn btn-success start-timer-btn'>Start Timer</button>-->
					<button class='btn btn-success resume-timer-btn hidden'>Resume</button>
					<button class='btn pause-timer-btn hidden'>Pause</button>
					<button class='btn btn-danger remove-timer-btn hidden'>Stop Timer</button>
				</div>
        </div>
		</form>


                <div class="sudoku-box ">
					<table id="sudoku-grid" cellspacing="0" cellpadding="0">
		<!--  Header -->
		%for y in range(9):
			<tr>
			%for x in range(9):
				%id = chr(ord('a')+y) + str(x+1)

                    %if x == 2 or x == 5 :
                        %if y == 2 or y == 5 :
						    <td class="hor-vert-9">
						%else :
						    <td class ="vert-9">
						%end
					%elif y == 2 or y == 5 :
						%if x == 2 or x == 5 :
						    <td class="hor-vert-9">
						%else :
						    <td class ="hor-9">
						%end
					%else:
						<td>
					%end

					<div id="boxdiv">
					<input class="cell"

					%if (id in board):
						value={{board[id]}}
						readonly
						style="background-color:#EEEF13"
					%else:
						value=""
					%end

					name={{id}}
					id={{id}}
					maxlength="1" size="1"
					onchange="updateCellValue(this.id, this.value)"
					onkeypress="return validateInput(event)"
					/>
					</div></td>
			%end
			<tr>
		%end
		</table>

				</div>

					<span><h2 id='userMessage' style="color:red;text-align: center;padding-top:10px;"></h2></span>
		<span><h1 id='winMessage' style="color:black;text-align: center;padding-top:10px;"></h1></span>




		</center>
              </div>
            </div>
          </section>
        </header>
        <section class="intro text-center section-padding" id="intro">
          <div class="container">
            <div class="row">
              <div class="col-md-8 col-md-offset-2 wp1">
                <h1 class="arrow">About Project</h1>
                <p>Sdk.kentgames.com from SDK Enterprises is a startup organization whose main idea is to stand in the competition of the gaming world. The company offers a developed Sudoku game for the end users or the gamers online with different variations in it. The company uses a systematic approach for developing and deploying the game which makes the users to have a user friendly interaction with the system, enabling a convenient online environment for playing the game providing user satisfaction. The team of SDK Enterprises is quiet efficient and the management is divided into various sectors in order to bring out the best possible results. In order to implement this idea of sudoku there is a need for funding for development and promoting the game among the industry. Apart from this we need funding for certain period of time for the future advancements and maintenance. As the game we develop have attractive features which saves the progress of each user throughout, gives us more advantage leading to success apart from others.
</p>
              </div>
            </div>
          </div>
        </section>

        <section class="swag text-center">
          <div class="container">
            <div class="row">
              <div class="col-md-8 col-md-offset-2">
                <h1>Know More About <span>SDK <em>Team</em></span></h1>
                <a href="#portfolio" class="down-arrow-btn"><i class="fa fa-chevron-down"></i></a>
              </div>
            </div>
          </div>
        </section>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="js/waypoints.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/scripts.js"></script>
		<script src="../js/light-bootstrap-dashboard.js"></script>
        	<script type="text/javascript" src="../js/main.js"></script>

	<script>
	function printChange(id, value) {
		console.log(id, value);
	};

	function validateInput(event) {
		if (event.charCode >= 49 && event.charCode <= 57) {
			document.getElementById('userMessage').innerHTML = ""
			return true;
		} else {
			document.getElementById('userMessage').innerHTML = "Enter only digits from 1-9"
			return false;
		};
	};

	function win() {
		document.getElementById('winMessage').innerHTML = "WOW! You made it!"
	};
	</script>
	<script src="../js/timer.jquery.js"></script>
<script>

$( document ).ready(function() {
    $('.timer').timer({
					editable: false
                });
                $('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
});

	    (function(){
			var hasTimer = false;
			// Init timer start
			$('.start-timer-btn').on('click', function() {
				hasTimer = true;
				$('.timer').timer({
					editable: true
                });
				$(this).addClass('hidden');
				$('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
			});

			// Init timer resume
			$('.resume-timer-btn').on('click', function() {
				$('.timer').timer('resume');
				$(this).addClass('hidden');
				$('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
			});


			// Init timer pause
			$('.pause-timer-btn').on('click', function() {
				$('.timer').timer('pause');
				$(this).addClass('hidden');
				$('.resume-timer-btn').removeClass('hidden');
			});

			// Remove timer
			$('.remove-timer-btn').on('click', function() {
				hasTimer = false;
				$('.timer').timer('remove');
				$(this).addClass('hidden');
				$('.start-timer-btn').removeClass('hidden');
				$('.pause-timer-btn, .resume-timer-btn').addClass('hidden');
			});

			// Additional focus event for this demo
			$('.timer').on('focus', function() {
				if(hasTimer) {
					$('.pause-timer-btn').addClass('hidden');
					$('.resume-timer-btn').removeClass('hidden');
				}
			});

			// Additional blur event for this demo
			$('.timer').on('blur', function() {
				if(hasTimer) {
					$('.pause-timer-btn').removeClass('hidden');
					$('.resume-timer-btn').addClass('hidden');
				}
			});
		})();
	</script>
      </body>
    </html>