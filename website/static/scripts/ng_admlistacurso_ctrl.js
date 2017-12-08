app.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    //$httpProvider.defaults.withCredentials = true;
}]);

app.controller('AdmListaCursoCtrl', function($window, $http, $rootScope){
	
	this.lista = [];

	$http({method: 'GET', url: urlServer + 'api/curso', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){	            	
					this.this.lista = data;
					console.log(this.lista);
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});


});