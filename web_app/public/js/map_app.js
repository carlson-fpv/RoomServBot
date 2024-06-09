const map = L.map('map').setView([40.82277, 44.49042], 13);

const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const gpx = 'res/hills.gpx';
new L.GPX(gpx, {
  async: true,
  marker_options: {
  startIconUrl: 'img/pin-icon-start.png',
  endIconUrl: 'img/pin-icon-end.png',
  shadowUrl: 'img/pin-shadow.png'
  }
}).on('loaded', function(e) {
  map.fitBounds(e.target.getBounds());
}).addTo(map);
