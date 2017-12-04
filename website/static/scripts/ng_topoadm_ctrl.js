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

app.controller('TopoAdmCtrl', function($scope, $window, $rootScope, $http){

	$scope.claAprenda = "inline-middle item-menu";
	$scope.claListagem = "inline-middle item-menu";
	$scope.claCadastro = "inline-middle item-menu";
	$scope.claRelatorio = "inline-middle item-menu";

	if(telaAtual == "Aprenda"){
		$scope.claAprenda = "inline-middle item-menu-selecionado";
	}else if(telaAtual == "Listagem"){
		$scope.claListagem = "inline-middle item-menu-selecionado";
	}else if(telaAtual == "Cadastro"){
		$scope.claCadastro = "inline-middle item-menu-selecionado";
	}else if(telaAtual == "Relatorio"){
		$scope.claRelatorio = "inline-middle item-menu-selecionado";
	}

});



