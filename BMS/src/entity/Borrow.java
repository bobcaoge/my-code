/**
 * 
 */
package entity;

import java.util.Date;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��21������9:44:11
 * @copyright СȺ����ô��ô��Ů��
 * @aim
 */
public class Borrow {

	/** �����ͼ�����Ϣ */
	private int id; // ���ĺ�
	private String book_id;
	private String reader_id;
	private Date borrow_date;
	private Date back_date;
	private boolean is_back; // �Ƿ�黹ͼ��

	/**
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * @return the book_id
	 */
	public String getBook_id() {
		return book_id;
	}

	/**
	 * @param book_id the book_id to set
	 */
	public void setBook_id(String book_id) {
		this.book_id = book_id;
	}

	/**
	 * @return the reader_id
	 */
	public String getReader_id() {
		return reader_id;
	}

	/**
	 * @param reader_id the reader_id to set
	 */
	public void setReader_id(String reader_id) {
		this.reader_id = reader_id;
	}

	/**
	 * @return the borrow_date
	 */
	public Date getBorrow_date() {
		return borrow_date;
	}

	/**
	 * @param borrow_date the borrow_date to set
	 */
	public void setBorrow_date(Date borrow_date) {
		this.borrow_date = borrow_date;
	}

	/**
	 * @return the back_date
	 */
	public Date getBack_date() {
		return back_date;
	}

	/**
	 * @param back_date the back_date to set
	 */
	public void setBack_date(Date back_date) {
		this.back_date = back_date;
	}

	/**
	 * @return the is_back
	 */
	public boolean isIs_back() {
		return is_back;
	}

	/**
	 * @param is_back the is_back to set
	 */
	public void setIs_back(boolean is_back) {
		this.is_back = is_back;
	}

}
