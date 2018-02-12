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

app.controller('AdmListaAulaCtrl', function($window, $http, $rootScope, $scope){

	$scope.curso = "";
	$scope.modulo = "";
	$scope.lista = [];
	var listaaux = [];

	$http({method: 'GET', url: urlServer + 'api/aula', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){
	            	for(i=0; i < data.length; i++){
	            		data[i].cla = "item-lista";	            		
	            	}
	            	$scope.lista = data;
	            	listaaux = clonaLista(data, listaaux);
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});

	$scope.excluir = function(aula){

		var resultado = confirm("Deseja remover a aula: " + aula.nome + " ?");

    	if(resultado){

    		var obj = {
    		
    			'tp_req': "deletar",
    			'id': aula.id,
	    		'nome': aula.nome,
	    		'descricao': aula.descricao,
	    		'id_modulo': aula.modulo.id,
	    		'url_video': aula.url_video

	    	};

	    	$http({method: 'POST', url: urlServer + 'api/aula', data: obj }).
		        success(function(data, status, headers, config) {
		            if(data == "sucesso"){
		                
		                alert("Curso removido com sucesso!");
		                $http({method: 'GET', url: urlServer + 'api/aula', withCredentials: true }).
					        success(function(data, status, headers, config) {
					            
					            $http({method: 'GET', url: urlServer + 'api/aula', withCredentials: true }).
							        success(function(data, status, headers, config) {
							            
							            console.log(data);
							            if(data != "Erro02"){
							            	for(i=0; i < data.length; i++){
							            		data[i].cla = "item-lista";	            		
							            	}
							            	$scope.lista = data;
							            	listaaux = clonaLista(data, listaaux);
							            	$scope.filtro();
							            }

							    	}).error(function(data, status, headers, config) {
							        	console.log("Não Funcionou");	        	  
						    		});
					            
					            

					    	}).error(function(data, status, headers, config) {
					        	console.log("Não Funcionou");	        	  
				    		});

		            }else{
						alert("Não foi possível remover o curso!");			                
		            }         
		        }).
		        error(function(data, status, headers, config) {
					alert("Não foi possível remover o curso!");		        	
		        });	 

    	}

	}

	$scope.editar = function(aula){

    	var resultado = confirm("Deseja editar a aula: " + aula.nome + " ?");

    	if(resultado){
    		aulaEditar = aula;
    		$rootScope.pagina = "cadastroaula";
    	}

    }

    var clonaLista = function(lista1, lista2){

		lista2 = [];

		for(i = 0; i < lista1.length; i++){
			lista2.push(lista1[i]);
		}

		return lista2;

	}

	$scope.filtro = function(){

		if($scope.curso.length > 0 && $scope.modulo.length > 0){

			$scope.lista = [];

			for(i=0; i < listaaux.length; i++){

				if(listaaux[i].modulo.curso.nome.toUpperCase().includes($scope.curso.toUpperCase()) && 
					listaaux[i].modulo.nome.toUpperCase().includes($scope.modulo.toUpperCase())){
					$scope.lista.push(listaaux[i]);
				}

			}

		}else if($scope.curso.length > 0 || $scope.modulo.length > 0){

			if($scope.curso.length > 0){

				$scope.lista = [];

				for(i=0; i < listaaux.length; i++){

					if(listaaux[i].modulo.curso.nome.toUpperCase().includes($scope.curso.toUpperCase())){
						$scope.lista.push(listaaux[i]);
					}

				}

			}else{

				$scope.lista = [];

				for(i=0; i < listaaux.length; i++){

					if(listaaux[i].modulo.nome.toUpperCase().includes($scope.modulo.toUpperCase())){
						$scope.lista.push(listaaux[i]);
					}

				}
			}

		}else{
			$scope.lista = clonaLista(listaaux, $scope.lista);
		}		

	}

});