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

app.controller('AdmCadastrosCtrl', function($window, $http, $rootScope){

	this.cadastroCur = function(){
		$rootScope.pagina = "cadastrocurso";
	}

	this.cadastroMod = function(){
		$rootScope.pagina = "cadastromodulo";
	}

	this.cadastroAul = function(){
		$rootScope.pagina = "cadastroaula";
	}

	this.listarCur = function(){
		$rootScope.pagina = "listacurso";
	}

	this.listarModulo = function(){
		$rootScope.pagina = "listamodulo";
	}

	this.listarAul = function(){
		$rootScope.pagina = "listaaula";
	}
	
});
