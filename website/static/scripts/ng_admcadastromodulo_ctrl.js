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

app.controller('AdmCadastroModuloCtrl', function($window, $http, $rootScope, $scope){

	$scope.cursos = [];
	$scope.selecionado = null;
	$scope.nome = "";
	$scope.descricao = "";

	$http({method: 'GET', url: urlServer + 'api/cursos', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){
	            	for(i=0; i < data.length; i++){
	            		data[i].cla = "item-lista";
	            		if(data[i].nome.length > 40){
	            			data[i].nome = data[i].nome.substring(0, 38) + "..."; 
	            		}
	            	}
	            	$scope.cursos = data;

	            	if(moduloEditar != null){
	            		for(i=0; i < $scope.cursos.length; i++){
							if($scope.cursos[i].id == moduloEditar.curso.id){
								$scope.cursos[i].cla = "item-lista-selecionado";
							}else{
								$scope.cursos[i].cla = "item-lista";
							}
						}
	            	}
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    	});

	

	if(moduloEditar != null){	
		$scope.nome = moduloEditar.nome;
		$scope.descricao = moduloEditar.descricao;
	}
	
	$scope.salvar = function(){

		if($scope.selecionado == null){
			alert("É necessário selecionar um curso.");
			return;
		}

		if($scope.nome.trim() == ""){
			alert("É necessário informar o nome.");
			return;
		}

		var modulo = null;

		if(moduloEditar == null){
			modulo = {
				'tp_req': "inserir",
				'nome': $scope.nome,
				'descricao': $scope.descricao,
				'id_curso': $scope.selecionado.id
			}
		}else{
			modulo = {
				'tp_req': "editar",
				'id': moduloEditar.id,
				'nome': $scope.nome,
				'descricao': $scope.descricao,
				'id_curso': $scope.selecionado.id
			}
		}		

		$http({method: 'POST', url: urlServer + 'api/modulo', data: modulo }).
	        success(function(data, status, headers, config) {
	            if(data == "sucesso"){
	                
	                $scope.selecionado = null;
					$scope.nome = "";
					$scope.descricao = "";

					for (i=0;i < $scope.cursos.length; i++){
		        		$scope.cursos[i].cla = "item-lista";
		        	}

		        	if(moduloEditar != null){
		        		moduloEditar == null;
		        	}

		        	alert("Curso cadastrado com sucesso!");

	            }else{
	                
	            }         
	        }).
	        error(function(data, status, headers, config) {
				alert("Não foi possível cadastrar o curso!");		        	
	        });	    


	}

	$scope.selecionaCurso = function(cur){

		$scope.selecionado = cur;

		for(i=0; i < $scope.cursos.length; i++){
			if($scope.cursos[i].id == cur.id){
				$scope.cursos[i].cla = "item-lista-selecionado";
			}else{
				$scope.cursos[i].cla = "item-lista";
			}
		}

	}

});