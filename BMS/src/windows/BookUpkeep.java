/**
 * 
 */
package windows;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.border.EtchedBorder;
import javax.swing.border.TitledBorder;
import javax.swing.table.DefaultTableModel;

import data.BookDao;
import entity.Book;
import util.Constant;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��26������7:12:44
 * @copyright СȺ����ô��ô��Ů��
 * @aim
 */
public class BookUpkeep extends PublicJFrame{
	
	private JTextField tf_id;
	private JTextField tf_name;
	private JComboBox<String>cb_type;
	private JTextField tf_author;
	private JTextField tf_translator;
	private JTextField tf_publisher;
	private JTextField tf_publish_time;
	private JTextField tf_stock;
	private JTextField tf_price;
	
	private JButton jb_insert,jb_update,jb_cancel,jb_close,jb_delete,jb_empty;
	private JTable table;
	
	private DefaultTableModel model = new DefaultTableModel(
			new Object[][] {},new String[] {
				"���","����","ͼ������","����","����","������","����ʱ��","ͼ����","�۸�"
			}
			);
	private List<Book>list = BookDao.selectBookList();
	
	BookUpkeep(){
		this.setTitle("--ͼ����Ϣά��--");
		setBounds(220, 100, 1200, 650);
		this.setResizable(true);
		this.setLocationRelativeTo(null);
		
		JPanel dialogPane = new JPanel();
		dialogPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		dialogPane.setBackground(new Color(198, 236, 253));
		dialogPane.setLayout(new BorderLayout());
		setContentPane(dialogPane);
		
		JSplitPane outerPane = new JSplitPane();
		outerPane.setOpaque(false);
		outerPane.setResizeWeight(0.1);
		outerPane.setOrientation(JSplitPane.HORIZONTAL_SPLIT);
		outerPane.setOneTouchExpandable(true);
		dialogPane.add(outerPane,BorderLayout.CENTER);
		
		JSplitPane innerPane = new JSplitPane();
		innerPane.setOpaque(false);
		innerPane.setBorder(new TitledBorder(
				new EtchedBorder(EtchedBorder.LOWERED,null,null),
				"ͼ����Ϣά��",TitledBorder.LEADING,TitledBorder.TOP,
				new Font("΢���ź�", Font.PLAIN, 14),
				new Color(59, 59, 59)));
		innerPane.setResizeWeight(0.8);
		innerPane.setOrientation(JSplitPane.VERTICAL_SPLIT);
		outerPane.setLeftComponent(innerPane);
		JPanel dataPanel = createDataPanel();
		innerPane.setLeftComponent(dataPanel);
		JPanel buttonPanel = createButtonPanel();
		innerPane.setRightComponent(buttonPanel);
		JPanel tablePanel = createTablePanel();
		outerPane.setRightComponent(tablePanel);
		
	}

	/**
	 * ������
	 * @return
	 */
	private JPanel createTablePanel() {
		// TODO Auto-generated method stub
		JPanel tablePanel = new JPanel(new BorderLayout(5,5));
		JScrollPane scrollPane = new JScrollPane();
		tablePanel.add(scrollPane);
		table = new JTable(model);
		
		for (int i = 0; i < list.size(); i++) {
			Book book = (Book)list.get(i);
			model.addRow(new Object[] {
					book.getId(),book.getName(),
					book.getType(),book.getAuthor(),
					book.getTranslator(),book.getPublisher(),
					book.getPublishi_time(),book.getStock(),
					book.getPrice()
			});
		}
		table.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {
				table_mouseClicked();
			}
		});
		scrollPane.setViewportView(table);
		return tablePanel;
	}

	/**
	 * �����Ӧ����
	 */
	public void table_mouseClicked() {
		// TODO Auto-generated method stub
		Book book_old = (Book)list.get(table.getSelectedRow());
		tf_id.setText(book_old.getId());
		tf_name.setText(book_old.getName());
		cb_type.setSelectedItem(book_old.getType());
		tf_author.setText(book_old.getAuthor());
		tf_translator.setText(book_old.getTranslator());
		tf_publisher.setText(book_old.getPublisher());
		tf_publish_time.setText(book_old.getPublishi_time());
		tf_stock.setText(String.valueOf(book_old.getStock()));
		tf_price.setText(String.valueOf(book_old.getPrice()));
		tf_id.setEditable(false);
	}

	/**
	 * ��ť���
	 * @return
	 */
	private JPanel createButtonPanel() {
		// TODO Auto-generated method stub
		JPanel buttonPanel = new JPanel(new GridBagLayout());
		buttonPanel.setOpaque(false);
		((GridBagLayout)buttonPanel.getLayout()).columnWidths = 
				new int[] {0,60,60,60,60,60,0};
		((GridBagLayout)buttonPanel.getLayout()).columnWeights = 
				new double[] {0.5,0.0,0.0,0.0,0.0,0.0,0.5};
		jb_insert = new JButton("���");
		jb_insert.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_insert_actionPerformed();
			}
		});
		buttonPanel.add(jb_insert, 
				new GridBagConstraints(1,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		
		jb_update = new JButton("�޸�");
		jb_update.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_update_actionPerformed();
			}
		});
		buttonPanel.add(jb_update,
				new GridBagConstraints(2,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		
		jb_delete = new JButton("ɾ��");
		jb_delete.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_delete_actionPerformed();
			}
		});
		
		buttonPanel.add(jb_delete,
				new GridBagConstraints(3,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		
		jb_cancel = new JButton("ȡ��");
		jb_cancel.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				del_content();
			}
		});
		buttonPanel.add(jb_cancel,
				new GridBagConstraints(4,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		jb_close = new JButton("�ر�");
		jb_close.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
			}
		});
		buttonPanel.add(jb_close,
				new GridBagConstraints(5,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		
		jb_empty = new JButton("�������ͼ��");
		jb_empty.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_empty_actionPerformed();
			}
		});
		buttonPanel.add(jb_empty,
				new GridBagConstraints(2,1,3,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(25, 0, 0, 0),0,0));
		return buttonPanel;
	}

	/**
	 * ɾ������ͼ����Ϣ
	 */
	protected void jb_empty_actionPerformed() {
		// TODO Auto-generated method stub
		int m = JOptionPane.showConfirmDialog(null, "ȷ��ɾ������ͼ����Ϣ��", "���ͼ����Ϣ", JOptionPane.YES_NO_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			int n = JOptionPane.showConfirmDialog(null, "ȷ����գ�","���ٴ�ȷ����գ�",JOptionPane.YES_NO_CANCEL_OPTION);
			if(n == JOptionPane.YES_OPTION) {
				BookDao.emptyBook();
				refresh();
				del_content();
			}
		}	
	}

	/**
	 * ����������
	 */
	public void del_content() {
		// TODO Auto-generated method stub
		tf_id.setText("");
		tf_name.setText("");
		cb_type.setSelectedIndex(0);
		tf_author.setText("");
		tf_translator.setText("");
		tf_publisher.setText("");
		tf_publish_time.setText("");
		tf_stock.setText("");
		tf_price.setText("");
		tf_id.setEditable(true);
		
	}

	/**
	 * ɾ��ͼ����
	 */
	protected void jb_delete_actionPerformed() {
		// TODO Auto-generated method stub
		String id = tf_id.getText().trim();
		int m = JOptionPane.showConfirmDialog(null, "ȷ��Ҫɾ������ͼ����Ϣ��", "ɾ��ͼ����Ϣ", JOptionPane.YES_NO_CANCEL_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			if(BookDao.deleteBook(id) == 1) {
				refresh();
				JOptionPane.showMessageDialog(null, "ͼ����Ϣɾ���ɹ���");
			}
			del_content();
		}
		
	}

	/**
	 * �޸�ͼ����Ϣ
	 */
	public void jb_update_actionPerformed() {
		// TODO Auto-generated method stub
		Book book = new Book();
		book.setId(tf_id.getText().trim());
		book.setName(tf_name.getText().trim());
		book.setType(cb_type.getSelectedItem().toString());
		book.setAuthor(tf_author.getText().trim());
		
		book.setTranslator(tf_translator.getText().trim());
		book.setPublisher(tf_publisher.getText().trim());
		book.setPublishi_time(tf_publish_time.getText().trim());
		book.setStock(new Integer(tf_stock.getText().trim()));
		book.setPrice(new Double(tf_price.getText().trim()));
		
		if(tf_name.getText().trim().equals("")
				|| tf_id.getText().trim().equals("")) {
			JOptionPane.showMessageDialog(null, "ͼ����Ϣ����Ϊ�գ�");
			return;
		}else {
			int i  = BookDao.updateBook(book);
			if(i == 1) {
				JOptionPane.showMessageDialog(null, "������Ϣ�޸ĳɹ���");
			}
			refresh();
			del_content();
		}
	}

	/**
	 * ���ͼ����Ϣ
	 */
	public void jb_insert_actionPerformed() {
		// TODO Auto-generated method stub
		Book book = new Book();
		book.setId(tf_id.getText().trim());
		book.setName(tf_name.getText().trim());
		book.setType(cb_type.getSelectedItem().toString());
		book.setAuthor(tf_author.getText().trim());
		
		book.setTranslator(tf_translator.getText().trim());
		book.setPublisher(tf_publisher.getText().trim());
		book.setPublishi_time(tf_publish_time.getText().trim());
		book.setStock(new Integer(tf_stock.getText().trim()));
		book.setPrice(new Double(tf_price.getText().trim()));
		
		if(tf_name.getText().trim().equals("") || tf_id.getText().trim().equals("")) {
			JOptionPane.showMessageDialog(null, "ͼ����Ϣ����Ϊ�գ�");
			return;
		}else {
			int i = BookDao.insertBook(book);
			if(i == 1) {
				model.addRow(new Object[] {
						book.getId(),book.getName(),
						book.getType(),book.getAuthor(),
						book.getTranslator(),book.getPublisher(),
						book.getPublishi_time(),book.getStock(),
						book.getPrice()	
				});
				refresh();
			}
			del_content();
		}
	}

	/**
	 * �������
	 * @return
	 */
	private JPanel createDataPanel() {
		// TODO Auto-generated method stub
		JPanel dataPanel = new JPanel(null);
		dataPanel.setBorder(new EmptyBorder(5, 5, 5, 10));
		dataPanel.setOpaque(false);
		
		JLabel jl_id = new JLabel("���");
		jl_id.setBounds(50, 20, 100, 25);
		dataPanel.add(jl_id);
		
		tf_id = new JTextField();
		tf_id.setBounds(140, 20, 170, 25);
		
		tf_id.setToolTipText("��������ͼ����");
		tf_id.addFocusListener(new FocusAdapter() {
			
			@Override
			public void focusLost(FocusEvent arg0) {
				// TODO Auto-generated method stub
				tf_id_focusLost();
			}
		});
		dataPanel.add(tf_id);
		
		JLabel jl_name = new JLabel("ͼ������");
		jl_name.setBounds(50, 60, 100, 25);
		dataPanel.add(jl_name);
		
		tf_name = new JTextField(10);
		tf_name.setBounds(140, 60, 170, 25);
		tf_name.setToolTipText("��������ͼ����");
		dataPanel.add(tf_name);
		
		tf_name.addFocusListener(new FocusAdapter() {
			public void focusLost(FocusEvent e) {
				tf_name_focusLost();
			}
		});
		
		JLabel jl_type = new JLabel("ͼ�����ͣ�");
		jl_type.setBounds(50, 100, 150, 25);
		dataPanel.add(jl_type);
		
		cb_type = new JComboBox<String>(Constant.BOOK_TYPES);
		cb_type.setBounds(140, 100, 170, 25);
		dataPanel.add(cb_type);
		
		JLabel jl_author = new JLabel("���ߣ�");
		jl_author.setBounds(50, 140, 150, 25);
		dataPanel.add(jl_author);
		
		tf_author = new JTextField(10);
		tf_author.setBounds(140, 140, 170, 25);
		dataPanel.add(tf_author);
		
		JLabel jl_translator = new JLabel("���ߣ�");
		jl_translator.setBounds(50, 180, 150, 25);
		dataPanel.add(jl_translator);
		
		tf_translator = new JTextField(10);
		tf_translator.setBounds(140, 180, 170, 25);
		dataPanel.add(tf_translator);
		
		JLabel jl_publisher = new JLabel("������");
		jl_publisher.setBounds(50, 220, 150, 25);
		dataPanel.add(jl_publisher);
		
		tf_publisher = new JTextField(10);
		tf_publisher.setBounds(140, 220, 170, 25);
		dataPanel.add(tf_publisher);
		
		JLabel jl_publish_time = new JLabel("��������");
		jl_publish_time.setBounds(50, 260, 150, 25);
		dataPanel.add(jl_publish_time);
		
		tf_publish_time = new JTextField("2015-01");
		tf_publish_time.setBounds(140, 260, 170, 25);
		dataPanel.add(tf_publish_time);
		
		JLabel jl_stock = new JLabel("�����");
		jl_stock.setBounds(50, 300, 150, 25);
		dataPanel.add(jl_stock);
		
		tf_stock = new JTextField(10);
		tf_stock.setBounds(140, 300, 170, 25);
		dataPanel.add(tf_stock);
		
		JLabel jl_price = new JLabel("�۸�");
		jl_price.setBounds(50, 340, 150, 25);
		dataPanel.add(jl_price);
		
		tf_price = new JTextField(10);
		tf_price.setBounds(140, 340, 150, 25);
		dataPanel.add(tf_price);
		
		return dataPanel;
	}

	/**
	 * 
	 */
	public void tf_name_focusLost() {
		// TODO Auto-generated method stub
		Book book = BookDao.getBookByName(tf_name.getText().trim());
		if(book != null) {
			JOptionPane.showMessageDialog(null, "ͼ�����Ѵ��ڣ������䣡");
			tf_name.setText("");
		}
		
	}

	/**
	 * 
	 */
	public void tf_id_focusLost() {
		// TODO Auto-generated method stub
		Book book = BookDao.getBookById(tf_id.getText().trim());
		if(book != null) {
			JOptionPane.showMessageDialog(null, "ͼ�����Ѵ��ڣ������䣡");
			del_content();
		}
		
	}
	
	public void refresh() {
		model.setRowCount(0);
		list = BookDao.selectBookList();
		for (int i = 0; i < list.size(); i++) {
			Book book = (Book)list.get(i);
			model.addRow(new Object[] {
					book.getId(),book.getName(),
					book.getType(),book.getAuthor(),
					book.getTranslator(),book.getPublisher(),
					book.getPublishi_time(),book.getStock(),
					book.getPrice()
			});
		}
		del_content();
	}
	
	//public static void main(String args[]) {
	//	new BookUpkeep();
	//}

}
