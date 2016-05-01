<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SEM SDKS</title>
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="css/templatestyles.css" rel="stylesheet">
    <link href="css/queries.css" rel="stylesheet">
    <link href="css/animate.css" rel="stylesheet">
    <style>
    #userMessage:after {
   content: none;
    }
    @media
        only screen and (max-width: 760px),
        (min-device-width: 768px) and (max-device-width: 1024px)  {
        	td input{
                padding:10%;
        	}
        	.timer{
        	width:40%;
        	}
        }

        .resume-timer-btn{
        position:relative;
        top:50%;
        left:50%;
        }

.modal {
    display: none;
    position: fixed;
    z-index: 1;
    padding-top: 20%;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
}

.modal-content {
    position: relative;
    background-color: #fefefe;
    margin: auto;
    padding: 0;
    border: 1px solid #888;
    width: 300px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
    -webkit-animation-name: animatetop;
    -webkit-animation-duration: 0.4s;
    animation-name: animatetop;
    animation-duration: 0.4s
}

@-webkit-keyframes animatetop {
    from {top:-300px; opacity:0}
    to {top:0; opacity:1}
}

@keyframes animatetop {
    from {top:-300px; opacity:0}
    to {top:0; opacity:1}
}

.close {
    color: white;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
}

.modal-header {
    padding: 2px 16px;
    background-color: #3DC9B3;
    color: white;
}

.modal-body {padding: 2px 16px;}

</style>
      </head>
      <body id="top">
      <div style="width:100%;height:100%;background:black;top:0;position:fixed;z-index:999;display:none;opacity:.9;overflow: none" id="pauseDiv">

      <button class='btn btn-success resume-timer-btn hidden'>Resume</button>
      </div>
        <div id="winMsg" class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <span class="close">×</span>
                    <h2>Congratulations</h2>
                </div>
                <div class="modal-body">
                    <p>WOW! You made it!</p>
                </div>
            </div>
        </div>
        <header id="home">
          <section class="hero" id="hero">
            <div class="container">
              <div class="row">
                <div class="col-md-12 text-right">
                  <h1 class="animated fadeInDown text-center">SEM<span>SDK'S</span></h1>
                  <p class="animated fadeInUp delay-05s text-center"><span class="bold title_color">S</span>u<span class="bold title_color">D</span>o
                  <span class="bold title_color">K</span>u Puzzle</p>
                </div>
              </div>
			  <div class="row animated delay-20s fadeInUp">

              <div class="col-md-12">
                    <form role="form" method="post" onsubmit="return false;">
                     <div class="row">
                        <div class="col-md-12">
                			<a href="./stop" class="confirmation">
                			   <button class="btn btn-info btn-fill" type="button"><img style="width:40px" src="../img/newgame.png"/> New Game</button>
                			</a>
                			<button class="btn btn-info btn-fill" type="submit" onclick="checkStatus()">
                			    <img style="width:40px" src="../img/check.png"/>
                			    Check
                			</button>
                        </div>

                        </div>
            				    <div class='row'>
                                <div class='col-md-12'>
                				    <input readonly style="border:none;background:none;color:#F5F5F5;margin-top:20px;" type='text' name='timer' class='timer' />

                					<button class='btn pause-timer-btn hidden'>Pause</button>
                					<button class='btn btn-danger remove-timer-btn hidden'>Remove Timer</button>
                				</div>
                    </div>
            		</form>


 <span><h2 id='userMessage' style="color:red;text-align: center;padding-top:10px;"></h2></span>
                <div class="sudoku-box ">
					<table id="sudoku-table">
					<tr></tr>
            %for y in range(9):
			<tr>
			%for x in range(9):
				%id = chr(ord('a')+y) + str(x+1)

                    <td>

					<div id="boxdiv">
					<input class="cell"
					type="tel"

					%if (id in board):
					    value={{board[id][0]}}

						%if (board[id][1] == False):
							 readonly="readonly"
							style="background-color:#EEEF13;cursor:default;color: transparent;text-shadow: 0 0 0 black;"

						%end

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
				<div style="text-align: Center; margin: 10px;">
                    <button class="btn btn-info btn-fill" onclick="window.open('http://tinyurl.com/jgdz3ny','_blank')">
                			    Game Rules
                </button>
				</div>
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
                <p><a href="sdks.kentsudoku.com">sdks.kentsudoku.com</a> from SDK Enterprises is a startup organization whose main idea is to stand in the competition of the gaming world. The company offers a developed Sudoku game for the end users or the gamers online with different variations in it. The company uses a systematic approach for developing and deploying the game which makes the users to have a user friendly interaction with the system, enabling a convenient online environment for playing the game providing user satisfaction. The team of SDK Enterprises is quiet efficient and the management is divided into various sectors in order to bring out the best possible results. In order to implement this idea of sudoku there is a need for funding for development and promoting the game among the industry. Apart from this we need funding for certain period of time for the future advancements and maintenance. As the game we develop have attractive features which saves the progress of each user throughout, gives us more advantage leading to success apart from others.
</p>
              </div>
            </div>
          </div>
        </section>

        <section class="swag text-center">
          <div class="container">
            <div class="row">
              <div class="col-md-8 col-md-offset-2">
                <h1>SDK <em>Team</em></h1>

              </div>
            </div>
          </div>
        </section>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/waypoints.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/sdk_scripts.js"></script>
    <script src="js/timer.jquery.js"></script>
	<script src="../js/light-bootstrap-dashboard.js"></script>
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
				hideDiv();
			});


			// Init timer pause
			$('.pause-timer-btn').on('click', function() {
				$('.timer').timer('pause');
				$(this).addClass('hidden');
				$('.resume-timer-btn').removeClass('hidden');
                showDiv();
			});

			// Remove timer
			$('.remove-timer-btn').on('click', function() {
				hasTimer = false;
				$('.timer').timer('remove');
				$(this).addClass('hidden');
				$('.start-timer-btn').removeClass('hidden');
				$('.pause-timer-btn, .resume-timer-btn, .timer').addClass('hidden');
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
			function hideDiv(){
			$("#pauseDiv").hide();
			enableScroll();
			}
			function showDiv(){
			$("#pauseDiv").show();
			disableScroll();
			}

		})();

		var keys = {37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e = e || window.event;
  if (e.preventDefault)
      e.preventDefault();
  e.returnValue = false;
}

function preventDefaultForScrollKeys(e) {
    if (keys[e.keyCode]) {
        preventDefault(e);
        return false;
    }
}

function disableScroll() {
  if (window.addEventListener) // older FF
      window.addEventListener('DOMMouseScroll', preventDefault, false);
  window.onwheel = preventDefault; // modern standard
  window.onmousewheel = document.onmousewheel = preventDefault; // older browsers, IE
  window.ontouchmove  = preventDefault; // mobile
  document.onkeydown  = preventDefaultForScrollKeys;
}

function enableScroll() {
    if (window.removeEventListener)
        window.removeEventListener('DOMMouseScroll', preventDefault, false);
    window.onmousewheel = document.onmousewheel = null;
    window.onwheel = null;
    window.ontouchmove = null;
    document.onkeydown = null;
}

function printChange(id, value) {
		console.log(id, value);
	};

	function validateInput(event) {
	 var key = window.event ? event.keyCode : event.which;
        if (event.keyCode == 8 || event.keyCode == 46
         || event.keyCode == 37 || event.keyCode == 39) {
            document.getElementById('userMessage').innerHTML = "";
            $(this).css("color","black")
            return true;
        }
        else if ( key < 49 || key > 57 ) {
            document.getElementById('userMessage').innerHTML = "~~~~~Please enter only digits between 1 to 9!~~~~~";
            return false;
        }
        else {
        document.getElementById('userMessage').innerHTML = "";
        return true;
        }
	};

	var modal = document.getElementById('winMsg');
	var exit = document.getElementsByClassName("close")[0];

	function success(){
	    $('.timer').timer('pause');
	    $('.resume-timer-btn').removeClass('hidden');
	    modal.style.display = "block";

	}

	exit.onclick = function() {
	    $('.timer').timer('resume');
		$('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
        modal.style.display = "none";
    }

    window.onclick = function(event) {
    if (event.target == modal) {
        $('.timer').timer('resume');
		$('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
        modal.style.display = "none";
    }
    }
    window.ontouchmove = function(event) {
    if (event.target == modal) {
        $('.timer').timer('resume');
		$('.pause-timer-btn, .remove-timer-btn').removeClass('hidden');
        modal.style.display = "none";
    }
    }


</script>
</body>
    </html>