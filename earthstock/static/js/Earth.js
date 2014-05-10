	function Earth (target, callback) {
		// dependencies
		var local$ = $;
		// return object
		var earth = {};
		// properties
		var placemarkIds = [];
		var points = [];
		var validEvents = ["click"
											,"dblclick"
											,"mouseover"
											,"mousedown"
											,"mouseup"
											,"mouseout"
											,"mousemove"];
		var ge, longitude, latitude, altitude;
		if(!target){
			target = "body";
		}
		google.load("earth", "1", {"other_params":"sensor=true_or_false"});
		// Helper functions for adding/removing events
		earth.addEvent = function(target, eventType, callback){
			if(checkForValidEvent(eventType) && checkForValidPlacemark(target)){
				google.earth.addEventListener(ge.getElementById(target), eventType, callback);
			} else {
				console.error("invalid event type or placemark");
			}
		}
		earth.removeEvent = function(target, eventType, callback){
			if(checkForValidEvent(eventType) && checkForValidPlacemark(target)){
				google.earth.removeEventListener(target, eventType, callback);
			} else {
				console.error("invalid event type or placemark");
			}
		}
		function checkForValidEvent(eventType){
			return inArray(eventType, validEvents);
		}
		function checkForValidPlacemark(placemarkId){
			return inArray(placemarkId, placemarkIds)
		}
		function inArray(target, array){
			// returns -1 if it can't find it, but returns index if it can
			index = local$.inArray(target, array);
			if(index == -1){
				return false;
			}
			return true;	
		}
		// end helper functions for adding/removing events
		function init() {
			google.earth.createInstance(target, initCB, failureCB);
			// checkForValidEvent("mousemove");
		}
		function initCB(instance) {
			// If earth could load
			ge = instance;
			ge.getWindow().setVisibility(true);
			ge.getOptions().setUnitsFeetMiles(true);
			var lookAt = ge.getView().copyAsLookAt(ge.ALTITUDE_RELATIVE_TO_GROUND);
			earth.latitude = lookAt.getLatitude();
			earth.longitude = lookAt.getLongitude();
			earth.altitude = lookAt.getRange();
			ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
			ge.getLayerRoot().enableLayerById(ge.LAYER_BORDERS, true);
			ge.getOptions().setStatusBarVisibility(true);
			ge.getOptions().setUnitsFeetMiles(true);
			ge.getOptions().setFadeInOutEnabled(false);
			if(callback && typeof(callback) === "function") {
				callback()
			}
		}
		function failureCB(errorCode) {
			// If earth couldn't load
		}
		google.setOnLoadCallback(init);
		earth.look = function () {
			var lookAt = ge.getView().copyAsLookAt(ge.ALTITUDE_RELATIVE_TO_GROUND);
			lookAt.setLatitude(this.latitude);
			lookAt.setLongitude(this.longitude);
			lookAt.setRange(this.altitude);
			ge.getView().setAbstractView(lookAt);
		}
		earth.setSpeed = function(speed) {
			speed = speed % 6;
			ge.getOptions().setFlyToSpeed(speed);
		}
		earth.getSpeed = function () {
			return ge.getOptions().getFlyToSpeed();
		}
		earth.setRange = function(miles) {
			// convert default meters to miles.
			this.altitude = miles * 1609.34;
		}
		earth.getRange = function () {
			return parseFloat(ge.getView().copyAsLookAt(ge.ALTITUDE_RELATIVE_TO_GROUND).getRange()) / 1609.34;
		}
		earth.placePlacemarker = function(id, lon, lat) {
			// Create the placemark.
			var placemark = ge.createPlacemark(id);
			// placemark.setName('satellite');
			// Define a custom icon.
			var icon = ge.createIcon('');
			icon.setHref('http://www.clker.com/cliparts/M/x/X/J/H/d/satellite-download-th.png');
			var style = ge.createStyle('');
			style.getIconStyle().setIcon(icon);
			style.getIconStyle().setScale(5.0);
			placemark.setStyleSelector(style);
			// Set the placemark's location.  
			var point = ge.createPoint('');
			point.setLongitude(lon);
			point.setLatitude(lat);
			placemark.setGeometry(point);
			ge.getFeatures().appendChild(placemark);
			placemarkIds.push(id);
			points.push(point);
		}
		earth.placeBalloon = function(lon, lat){
			window.placemark = ge.createPlacemark('');
			var point = ge.createPoint('');
			point.setLatitude(lat || ge.getView().copyAsLookAt(ge.ALTITUDE_RELATIVE_TO_GROUND).getLatitude());
			point.setLongitude(lon || ge.getView().copyAsLookAt(ge.ALTITUDE_RELATIVE_TO_GROUND).getLongitude());
			placemark.setGeometry(point);
			ge.getFeatures().appendChild(placemark);

			var balloon = ge.createHtmlDivBalloon('');
			balloon.setFeature(placemark);
			var div = document.createElement('DIV');
			div.innerHTML = 'Any <hr> html <br> css or js goes <br> here';
			balloon.setContentDiv(div);
			ge.setBalloon(balloon);
		}
		earth.kmlStuff = function(){
			var kmlString = ''
              + '<?xml version="1.0" encoding="UTF-8"?>'
              + '<kml xmlns="http://www.opengis.net/kml/2.2">'

              + '<Document>'
              + '  <Camera>'
              + '    <longitude>122.444633</longitude>'
              + '    <latitude>-37.801899</latitude>'
              + '    <altitude>11139.629438</altitude>'
              + '  </Camera>'

              + '  <Placemark>'
              + '    <name>Placemark from KML string</name>'
              + '    <Point>'
              + '      <coordinates>-122.448425,37.802907,0</coordinates>'
              + '    </Point>'
              + '  </Placemark>'

              + '</Document>'
              + '</kml>';

			var kmlObject = ge.parseKml(kmlString);
			ge.getFeatures().appendChild(kmlObject);
			if (kmlObject.getAbstractView())
   		ge.getView().setAbstractView(kmlObject.getAbstractView());
		}
		return earth;
	}