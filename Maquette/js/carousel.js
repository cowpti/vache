$(document).ready(function(){
	$('#iview2').iView({
		pauseTime: 3000,
		pauseOnHover: true,
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
});