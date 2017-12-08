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

app.controller('AdmListaCursoCtrl', function($window, $http, $rootScope, $scope){
	
	$scope.lista = [];
	this.selecionado = {};

	$http({method: 'GET', url: urlServer + 'api/curso', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){
	            	for(i=0; i < data.length; i++){
	            		data[i].cla = "item-lista";
	            		if(data[i].descricao.length > 40){
	            			data[i].descricao = data[i].descricao.substring(0, 38) + "..."; 
	            		}
	            	}
	            	$scope.lista = data;
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});

	this.selecionaItem = function(item){

		this.selecionado = item;

		for(i=0; i < $scope.lista.length; i++){
			if($scope.lista[i].id == item.id){
				$scope.lista[i].cla = "item-lista-selecionado";
			}else{
				$scope.lista[i].cla = "item-lista";
			}
		}

	}

});