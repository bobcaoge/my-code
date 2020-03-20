/**
 * 
 */
package entity;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月21日下午9:38:58
 * @copyright 小群子怎么那么淑女呢
 * @aim
 */
public class Book {

	/** 图书 */
	private String id; // 图书编号
	private String name;
	private String type;
	private String author;
	private String translator;
	private String publisher;
	private String publishi_time;
	private int stock; // 图书库存量
	private double price; // 图书单价

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
	 * @return the tpye
	 */
	public String getType() {
		return type;
	}

	/**
	 * @param tpye the tpye to set
	 */
	public void setType(String type) {
		this.type = type;
	}

	/**
	 * @return the author
	 */
	public String getAuthor() {
		return author;
	}

	/**
	 * @param author the author to set
	 */
	public void setAuthor(String author) {
		this.author = author;
	}

	/**
	 * @return the translator
	 */
	public String getTranslator() {
		return translator;
	}

	/**
	 * @param translator the translator to set
	 */
	public void setTranslator(String translator) {
		this.translator = translator;
	}

	/**
	 * @return the publisher
	 */
	public String getPublisher() {
		return publisher;
	}

	/**
	 * @param publisher the publisher to set
	 */
	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	/**
	 * @return the publishi_time
	 */
	public String getPublishi_time() {
		return publishi_time;
	}

	/**
	 * @param publishi_time the publishi_time to set
	 */
	public void setPublishi_time(String publishi_time) {
		this.publishi_time = publishi_time;
	}

	/**
	 * @return the stock
	 */
	public int getStock() {
		return stock;
	}

	/**
	 * @param stock the stock to set
	 */
	public void setStock(int stock) {
		this.stock = stock;
	}

	/**
	 * @return the price
	 */
	public double getPrice() {
		return price;
	}

	/**
	 * @param price the price to set
	 */
	public void setPrice(double price) {
		this.price = price;
	}

}
