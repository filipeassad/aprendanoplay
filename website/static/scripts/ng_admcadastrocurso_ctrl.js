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

app.controller('AdmCadastroCursoCtrl', function($window, $http, $rootScope, $scope){	

	if(cursoEditar == null){
		$scope.professores = [];
		$scope.selecionado = null;
		$scope.nome = "";
		$scope.descricao = "";		
	}else{
		$scope.nome = cursoEditar.nome;
		$scope.descricao = cursoEditar.descricao;
	}	

	$http({method: 'GET', url: urlServer + 'api/professores', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){
	            	for(i=0; i < data.length; i++){
	            		data[i].cla = "item-lista";
	            		if(data[i].nome.length > 40){
	            			data[i].nome = data[i].nome.substring(0, 38) + "..."; 
	            		}
	            	}
	            	$scope.professores = data;
	            	if(cursoEditar != null){
	            		$scope.selecionaProfessor(cursoEditar.perfil);
	            	}
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});

	$scope.selecionaProfessor = function(pro){
		$scope.selecionado = pro;

		for(i=0; i < $scope.professores.length; i++){
			if($scope.professores[i].id == pro.id){
				$scope.professores[i].cla = "item-lista-selecionado";
			}else{
				$scope.professores[i].cla = "item-lista";
			}
		}
	}

	$scope.salvar = function(){

		if($scope.selecionado == null){
			alert("É necessário selecionar um professor.");
			return;
		}

		if($scope.nome.trim() == ""){
			alert("É necessário informar o nome.");
			return;
		}

		var curso = null;

		if(cursoEditar == null){
			curso = {

    			'tp_req': "inserir",
    			'nome': $scope.nome,
    			'descricao': $scope.descricao,
    			'id_perfil': $scope.selecionado.id

    		};
		}else{
			curso = {

    			'tp_req': "editar",
    			'id': cursoEditar.id,
    			'nome': $scope.nome,
    			'descricao': $scope.descricao,
    			'id_perfil': $scope.selecionado.id

    		};
		}
		

    	$http({method: 'POST', url: urlServer + 'api/curso', data: curso }).
	        success(function(data, status, headers, config) {
	            if(data == "sucesso"){
	                
	                $scope.selecionado = null;
					$scope.nome = "";
					$scope.descricao = "";

					for (i=0;i < $scope.professores.length; i++){
		        		$scope.professores[i].cla = "item-lista";
		        	}

		        	if(cursoEditar != null){
		        		cursoEditar == null;
		        	}

		        	alert("Curso cadastrado com sucesso!");

	            }else{
	                
	            }         
	        }).
	        error(function(data, status, headers, config) {
				alert("Não foi possível cadastrar o curso!");		        	
	        });	    


	}	

});