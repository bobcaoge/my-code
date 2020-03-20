/**
 * 
 */
package entity;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2017年6月21日下午9:26:44
 * @copyright 小群子怎么那么淑女呢
 * @aim
 */
public class User {
	/** 成员变量 */
	private int id; // 表示用户编号
	private String name; // 表示用户名称
	private String pass; // 表示用户密码
	private byte is_admin; // 表示用户访问权限

	/**
	 * 成员方法的功能：获取用户编号
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * 成员方法的功能：设置用户编号
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * 成员方法的功能；获得用户名称
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * 成员方法的功能：设置用户名称
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * 成员方法的功能：获得用户密码
	 * @return the pass
	 */
	public String getPass() {
		return pass;
	}

	/**
	 * 成员方法的功能：设置用户密码
	 * @param pass the pass to set
	 */
	public void setPass(String pass) {
		this.pass = pass;
	}

	/**
	 * 成员方法的功能:获得用户权限
	 * @return the is_admin
	 */
	public byte getIs_admin() {
		return is_admin;
	}

	/**
	 * 成员方法的功能：设置用户权限
	 * @param is_admin the is_admin to set
	 */
	public void setIs_admin(byte is_admin) {
		this.is_admin = is_admin;
	}

}
