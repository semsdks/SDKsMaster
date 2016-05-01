
function updateCellValue(cell_id, value) {
	$('#'+cell_id).css('background-color', 'white');

	if (value == "") {

	} else {
		$.ajax({
			type: "POST",
			url: "/modify",
			data : { 'id': cell_id, 'value': value },
			success: function(results) {
				console.log(results);
			},
			error: function(error) {
				console.log(error)
			}
		});
	};
};

function checkStatus() {
	$.ajax({
		type: "GET",
		url: "/status",
		data : {},
		success: function(results) {
			console.log(results);
			status_map = results['status_map']
			for (cell in status_map) {
				current_cell = status_map[cell]
				cell_id = current_cell[0]
				isMutable = current_cell[1]
				isCorrect = current_cell[2]

				if (isMutable === true) {
					if (isCorrect === true) {
						$('#'+cell_id).css('color', '#02F302');
					}
					else if (isCorrect === false) {
						$('#'+cell_id).css('color', '#DC2222');
					}
				}

				if (results['status'] === 'Correct') {
					win()
				}
			};
		},
		error: function(error) {
			console.log(error)
		}
	});
};


$(document).ready(function() {

	$('.wp1').waypoint(function() {
		$('.wp1').addClass('animated fadeInLeft');
	}, {
		offset: '75%'
	});


});
