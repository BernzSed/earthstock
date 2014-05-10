var app = (function(){
	var earth;
	var kml;
	earth = Earth('map3d', function(){
		earth.longitude = -102.0822035425683;
		earth.latitude  = 40.42228990140251;
		earth.setRange(   1200   );  // in miles
		earth.look();
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