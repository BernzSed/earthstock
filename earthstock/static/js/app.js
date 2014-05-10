var app = (function(){
	var earth;
	earth = Earth('map3d', function(){
		earth.longitude = 10;
		earth.latitude  = 10;
		earth.setRange(   1000   );  // in miles
		earth.look();
		earth.placeBalloon(10, 10);
		earth.kmlStuff();
	});
})();