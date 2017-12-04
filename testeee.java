public class SicomManDAO extends DAOGenerico<HashMap<String, Object>, HashMap<String, Object>> {

public SicomManDAO(){
super("Sicomman");
}

public List<HashMap<String, Object>> getRegsParaArquivoByParam(HashMap<String, Object> hash) {
try {
return sqlMap.queryForList(this.getNameSpaceMap() + ".getRegsParaArquivoByParam", hash);
} catch (SQLException e) {
e.printStackTrace();
}
return null;
}

}