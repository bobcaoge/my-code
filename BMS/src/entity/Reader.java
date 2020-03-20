/**
 * 
 */
package entity;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2016年6月21日下午9:35:03
 * @copyright 小群子怎么那么淑女呢
 * @aim
 */
public class Reader {

	/** 成员变量 */
	private String id; // 表示读者编码
	private String name; // 表示读者姓名
	private String type; // 表示读者类型
	private String sex; // 表示读者性别
	private int max_num; // 表示读者最大借书数量
	private int days_num; // 表示读者最多借书多少天

	/**
	 * @return the id
	 */
	public String getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(String id) {
		this.id = id;
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * @return the type
	 */
	public String getType() {
		return type;
	}

	/**
	 * @param type the type to set
	 */
	public void setType(String type) {
		this.type = type;
	}

	/**
	 * @return the sex
	 */
	public String getSex() {
		return sex;
	}

	/**
	 * @param sex the sex to set
	 */
	public void setSex(String sex) {
		this.sex = sex;
	}

	/**
	 * @return the max_num
	 */
	public int getMax_num() {
		return max_num;
	}

	/**
	 * @param max_num the max_num to set
	 */
	public void setMax_num(int max_num) {
		this.max_num = max_num;
	}

	/**
	 * @return the days_num
	 */
	public int getDays_num() {
		return days_num;
	}

	/**
	 * @param days_num the days_num to set
	 */
	public void setDays_num(int days_num) {
		this.days_num = days_num;
	}

}
