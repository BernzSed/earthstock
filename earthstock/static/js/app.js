var app = (function(){
	var earth;
	var kml;
	earth = Earth('map3d', function(){
		// earth.longitude = -122.0822035425683;
		// earth.latitude  = 37.42228990140251;
		// earth.setRange(   150   );  // in miles
		// earth.look();
		// earth.placeBalloon(10, 10);
		// $.get("/stocks.kml", function(kml){
		// 	console.log('response');
		// 	console.debug(kml);
		// 	earth.kmlStuff(kml);
		// });
	earth.loadKmlByLink('/stocks.kml');
		// earth.kmlStuff();
	});
})();