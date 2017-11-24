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

app.controller('CadastroAulaCtrl', function($scope, $window, $rootScope, $http){

		$scope.cursos = [];
		$scope.cursoSelecionado = {};
		$scope.modulos = [];
		$scope.moduloSelecionado = {};

		$scope.nome = "";
		$scope.urlVideo = "";
		$scope.descricao = "";

		$http({method: 'GET', url: urlServer + 'api/curso', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            //$scope.listacursos = data;
	            console.log(data);
	            if(data != "Erro02"){

	            	for (i=0;i < data.length; i++){
	            		console.log(data[i].nome);
	            		data[i].cla = "item-lista";
	            	}
					$scope.cursos = data;
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");
	        	  
    	});


	    $scope.selecionaCurso = function(cur){
	    	$scope.cursoSelecionado = cur;
		    for (i=0;i < $scope.cursos.length; i++){
        		$scope.cursos[i].cla = "item-lista";
        	}
	    	cur.cla = "item-lista-selecionado";
	    	$scope.moduloSelecionado = {};
	    	$http({method: 'GET', url: urlServer + 'api/modulo', 
	    		withCredentials: true, params: {id: cur.id}}).
		        success(function(data, status, headers, config) {
		            
		            if(data != "Não encontrado"){
		            	$scope.modulos = data;
		            	if($scope.modulos.length > 0){
		            		$scope.moduloSelecionado = $scope.modulos[0];
		            	}
		            }

		    	}).error(function(data, status, headers, config) {
		        	console.log("Não Funcionou");
		        	  
	    	});
	    }

	    $scope.selecionaModulo = function(modulo){
	    	$scope.moduloSelecionado = modulo;
	    }

	    $scope.cadastraAula = function(){

	    	if($scope.cursoSelecionado == {}){
	    		alert("Selecione um curso!");
	    		return;
	    	}

	    	if($scope.moduloSelecionado == {}){
	    		alert("Selecione um modulo!");
	    		return;
	    	}

			if($scope.nome.trim() == ""){
	    		alert("Digite o nome!");
	    		return;
	    	}

	    	if($scope.urlVideo.trim() == ""){
	    		alert("Digite a url do vídeo!");
	    		return;
	    	}	    	

	    	if($scope.descricao.trim() == ""){
	    		alert("Digite a descrição!");
	    		return;
	    	}	    	

	    	var aula = {
	    		
	    		'nome': $scope.nome,
	    		'url_aula': $scope.urlVideo,
	    		'descricao': $scope.descricao,
	    		'id_modulo': $scope.moduloSelecionado.id
	    	};

	    	$http({method: 'POST', url: urlServer + 'api/aula', data: aula }).
		        success(function(data, status, headers, config) {
		            if(data == "Cadastrado"){
		                
		                $scope.cursoSelecionado = {};
						$scope.modulos = [];
						$scope.moduloSelecionado = {};

						$scope.nome = "";
						$scope.urlVideo = "";
						$scope.descricao = "";

						for (i=0;i < $scope.cursos.length; i++){
			        		$scope.cursos[i].cla = "item-lista";
			        	}

			        	alert("Aula cadastrada com sucesso!");

		            }else{
		                
		            }         
		        }).
		        error(function(data, status, headers, config) {
					alert("Não foi possível cadastrar a aula!");		        	
		        });

	    }


});