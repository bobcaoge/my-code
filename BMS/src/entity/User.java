/**
 * 
 */
package entity;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2017��6��21������9:26:44
 * @copyright СȺ����ô��ô��Ů��
 * @aim
 */
public class User {
	/** ��Ա���� */
	private int id; // ��ʾ�û����
	private String name; // ��ʾ�û�����
	private String pass; // ��ʾ�û�����
	private byte is_admin; // ��ʾ�û�����Ȩ��

	/**
	 * ��Ա�����Ĺ��ܣ���ȡ�û����
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * ��Ա�����Ĺ��ܣ������û����
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * ��Ա�����Ĺ��ܣ�����û�����
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * ��Ա�����Ĺ��ܣ������û�����
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * ��Ա�����Ĺ��ܣ�����û�����
	 * @return the pass
	 */
	public String getPass() {
		return pass;
	}

	/**
	 * ��Ա�����Ĺ��ܣ������û�����
	 * @param pass the pass to set
	 */
	public void setPass(String pass) {
		this.pass = pass;
	}

	/**
	 * ��Ա�����Ĺ���:����û�Ȩ��
	 * @return the is_admin
	 */
	public byte getIs_admin() {
		return is_admin;
	}

	/**
	 * ��Ա�����Ĺ��ܣ������û�Ȩ��
	 * @param is_admin the is_admin to set
	 */
	public void setIs_admin(byte is_admin) {
		this.is_admin = is_admin;
	}

}
