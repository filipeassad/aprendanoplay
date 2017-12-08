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

app.controller('AdmAprendaCtrl', function($window, $http, $rootScope){

	//$scope.pagina = "{% include \"subtemplates/topoadm.html\" %}";
	$rootScope.pagina = "telainicial";

});

app.controller('AdmMenuCtrl', function($window, $http, $rootScope){



	this.telainicial = function(){
		$rootScope.pagina = "telainicial";
		$rootScope.nome = "Tela Inicial";
	}

	this.cadastro = function(){
		$rootScope.pagina = "cadastro";
		$rootScope.nome = "Cadastros";
	}
	
	this.relatorios = function(){
		$rootScope.pagina = "relatorios";
		$rootScope.nome = "Relatorios";
	}

});


app.controller('AdmTituloCtrl', function($window, $http, $rootScope){

	$rootScope.nome = "Tela Inicial";

});