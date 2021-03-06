$(document).ready(function(){
	$('#iview2').iView({
		pauseTime: 3000,
		pauseOnHover: false,
		directionNav: true,
		directionNavHide: false,
		controlNav: true,
		controlNavNextPrev: false,
		controlNavTooltip: false,
		nextLabel: "Next",
		previousLabel: "Previous",
		playLabel: "Play",
		pauseLabel: "Pause",
		timer: "360Bar",
		timerBg: "#EEE",
		timerColor: "#000",
		timerDiameter: 40,
		timerPadding: 4,
		timerStroke: 8,
		timerPosition: "bottom-right"
	});
	
	 // Au survol du bouton, identifié par la classe pauseButton
	$('.ppButton').on('click',function(){
		if ($(this).attr('src') == 'img/pause.png') {
			var src = 'img/play.png'
			$(this).attr('src', src);

			// On pause le slider iView, identifié par l'ID "slider"
			$('#iview2').trigger('iView:pause');
		} else {
			var src = 'img/pause.png'
			$(this).attr('src', src);
			// On remet en marche le slider
			$('#iview2').trigger('iView:play');
		}
	});
});