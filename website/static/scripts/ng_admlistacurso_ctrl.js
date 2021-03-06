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
	$scope.selecionado = {};

	$http({method: 'GET', url: urlServer + 'api/curso', withCredentials: true }).
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
	            }

	    	}).error(function(data, status, headers, config) {
	        	console.log("Não Funcionou");	        	  
    		});

    $scope.excluir = function(curso){

    	var resultado = confirm("Deseja remover o curso: " + curso.nome + " ?");

    	if(resultado){

    		var obj = {
    		
    			'tp_req': "deletar",
    			'id': curso.id,
	    		'nome': curso.nome,
	    		'descricao': curso.descricao,
	    		'id_perfil': curso.perfil.id

	    	};

	    	$http({method: 'POST', url: urlServer + 'api/curso', data: obj }).
		        success(function(data, status, headers, config) {
		            if(data == "sucesso"){
		                
		                alert("Curso removido com sucesso!");
		                $http({method: 'GET', url: urlServer + 'api/curso', withCredentials: true }).
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
					            }

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

    $scope.editar = function(curso){

    	var resultado = confirm("Deseja editar o curso: " + curso.nome + " ?");

    	if(resultado){
    		cursoEditar = curso;
    		$rootScope.pagina = "cadastrocurso";
    	}

    }
	

});