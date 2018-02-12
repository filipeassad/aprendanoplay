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

app.controller('AdmListaModuloCtrl', function($window, $http, $rootScope, $scope){

	$scope.lista = [];
	$scope.selecionado = null;
	var listaaux = [];
	$scope.curso = "";

	$http({method: 'GET', url: urlServer + 'api/modulo', withCredentials: true }).
	        success(function(data, status, headers, config) {
	            
	            console.log(data);
	            if(data != "Erro02"){
	            	for(i=0; i < data.length; i++){
	            		data[i].cla = "item-lista";
	            		data[i].descricaoaux ="";
	            		if(data[i].descricao.length > 40){
	            			data[i].descricaoaux = data[i].descricao.substring(0, 38) + "..."; 
	            		}else{
	            			data[i].descricaoaux = data[i].descricao;
	            		}

	            	}
	            	$scope.lista = data;
	            	listaaux = clonaLista(data, listaaux);
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});

	$scope.filtro = function(){

		if($scope.curso.length > 0){

			$scope.lista = [];

			for(i=0; i < listaaux.length; i++){

				if(listaaux[i].curso.nome.toUpperCase().includes($scope.curso.toUpperCase())){
					$scope.lista.push(listaaux[i]);
				}

			}

		}else{
			$scope.lista = clonaLista(listaaux, $scope.lista);
		}		

	}

	var clonaLista = function(lista1, lista2){

		lista2 = [];

		for(i = 0; i < lista1.length; i++){
			lista2.push(lista1[i]);
		}

		return lista2;

	}

	$scope.excluir = function(modulo){

		var resultado = confirm("Deseja remover o módulo: " + modulo.nome + " ?");

    	if(resultado){

    		var obj = {
    		
    			'tp_req': "deletar",
    			'id': modulo.id,
	    		'nome': modulo.nome,
	    		'descricao': modulo.descricao,
	    		'id_curso': modulo.curso.id

	    	};

	    	$http({method: 'POST', url: urlServer + 'api/modulo', data: obj }).
		        success(function(data, status, headers, config) {
		            if(data == "sucesso"){
		                
		                alert("Módulo removido com sucesso!");
		                $http({method: 'GET', url: urlServer + 'api/modulo', withCredentials: true }).
					        success(function(data, status, headers, config) {
					            
					            console.log(data);
					            if(data != "Erro02"){
					            	for(i=0; i < data.length; i++){
					            		data[i].cla = "item-lista";
					            		data[i].descricaoaux ="";
					            		if(data[i].descricao.length > 40){
					            			data[i].descricaoaux = data[i].descricao.substring(0, 38) + "..."; 
					            		}else{
					            			data[i].descricaoaux = data[i].descricao;
					            		}

					            	}
					            	$scope.lista = data;
					            	listaaux = clonaLista(data, listaaux);
					            	$scope.filtro();
					            }

					    	}).error(function(data, status, headers, config) {
					        	console.log("Não Funcionou");	        	  
				    		});

		            }else{
						alert("Não foi possível remover o módulo!");			                
		            }         
		        }).
		        error(function(data, status, headers, config) {
					alert("Não foi possível remover o módulo!");		        	
		        });

    	}

	}

	$scope.editar = function(modulo){

		var resultado = confirm("Deseja editar o módulo: " + modulo.nome + " ?");

    	if(resultado){
    		moduloEditar = modulo;
    		$rootScope.pagina = "cadastromodulo";
    	}

	}



});