/**
 * 
 */
package windows;

import java.awt.BorderLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;

import data.BookDao;
import entity.Book;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月27日下午3:45:50
 * @copyright 小群子怎么那么淑女呢
 * @aim
 */
public class BookQuery extends PublicJFrame{
	
	JLabel lb_query;
	JTextField tf_query;
	JComboBox<String>cb_query;
	JButton bt_query;
	private JTable table;
	
	private List<Book>list = BookDao.selectBookList();
	
	private String[] tb_heads = {
			"图书编号","书名","图书类型","作者","译者","出版社","出版时间","库存","价格"
	};
	
	private String[] fields = {
			"id","name","type","author","translator","publisher","publishi_time","stock","price"
	};
	
	private DefaultTableModel model = new DefaultTableModel(new Object[][] {}, tb_heads);
	
	private String field = "id";
	String valueStr = " ";
	int valueInt = 0;
	double valueDouble = 0.0;
	
	BookQuery(){
		this.setTitle("--图书查询--(模糊查询)");
		this.setVisible(true);
		this.setSize(1000,500);
		JPanel queryPanel = createQueryPanel();
		this.add(queryPanel,BorderLayout.NORTH);
		JPanel tablePanel = createTablePanel();
		this.add(tablePanel,BorderLayout.CENTER);
		this.setLocationRelativeTo(null);
	}

	/**
	 * 表格面板
	 * @return
	 */
	private JPanel createTablePanel() {
		// TODO Auto-generated method stub
		JPanel tablePanel = new JPanel(new BorderLayout(5,5));
		JScrollPane scrollPane = new JScrollPane();
		tablePanel.add(scrollPane);
		table = new JTable(model);
		addRowToModel(list);
		scrollPane.setViewportView(table);
		return tablePanel;
	}

	/**
	 * 添加图书
	 * @param list2
	 */
	private void addRowToModel(List<Book> list2) {
		// TODO Auto-generated method stub
		model.setRowCount(0);
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
		
	}

	/**
	 * 查询面板
	 * @return
	 */
	private JPanel createQueryPanel() {
		// TODO Auto-generated method stub
		JPanel queryPanel = new JPanel();
		queryPanel.setOpaque(false);
		queryPanel.setLayout(new GridBagLayout());
		((GridBagLayout)queryPanel.getLayout()).columnWidths = 
				new int[] {
						0,100,200,120,80,80,0
				};
		((GridBagLayout)queryPanel.getLayout()).columnWeights = 
				new double[] {
						0.5,0.0,0.0,0.0,0.0,0.0,0.5
		};
		lb_query = new JLabel("请输入图书编号");
		queryPanel.add(lb_query,
				new GridBagConstraints(1,0,1,1,0.0,0.0,
						GridBagConstraints.EAST,
						GridBagConstraints.BOTH,
						new Insets(10, 10, 10, 10),0,0));
		
		tf_query = new JTextField();
		tf_query.requestFocus();
		tf_query.addKeyListener(new KeyAdapter() {
			public void keyTyped(KeyEvent arg0) {
				if(arg0.getKeyChar() == '\n') {
					bn_query_actionPerformed();
				}
			}
		});
		queryPanel.add(tf_query,
				new GridBagConstraints(2,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10, 0, 10, 10),0,0));
		
		cb_query = new JComboBox<String>(tb_heads);
		cb_query.addItemListener(new ItemListener() {
			
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
				cb_query_itemStateChanged(e);
			}
		});
		queryPanel.add(cb_query,
				new GridBagConstraints(3,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10,0,10,10),0,0));
		
		bt_query = new JButton("查询");
		bt_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				bn_query_actionPerformed();
			}
		});
		queryPanel.add(bt_query,
				new GridBagConstraints(4,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10, 0, 10, 10),0,0));
		
		JButton bn_close = new JButton("关闭");
		bn_close.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
			}
		});
		queryPanel.add(bn_close,
				new GridBagConstraints(5,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10, 0, 10, 10),0,0));
		return queryPanel;
	}

	/**
	 * 栏目组合框转态改变
	 * @param e
	 */
	private void cb_query_itemStateChanged(ItemEvent e) {
		// TODO Auto-generated method stub
		if(e.getStateChange() == ItemEvent.SELECTED) {
			lb_query.setText("请输入" + (String)e.getItem() + "：");
			tf_query.setText("");
			for (int i = 0; i < tb_heads.length; i++) {
				if(e.getItem().equals(tb_heads[i])) {
					field = fields[i];
				}
			}
			list = BookDao.selectBookList();
			addRowToModel(list);
			tf_query.requestFocus();
					
		}		
	}

	/**
	 * 查询的响应
	 */
	private void bn_query_actionPerformed() {
		// TODO Auto-generated method stub
		switch(field) {
		case "id":
		case "name":
		case "type":
		case "author":
		case "translator":
		case "publisher":
		case "publishi_time":
			valueStr = tf_query.getText();
			list = BookDao.selectBookList(field,valueStr);
			break;
		case "stock":
			if(tf_query.getText().equals("")) {
				tf_query.setText("0");
			}
			valueInt = new Integer(tf_query.getText()).intValue();
			list = BookDao.selectBookList(field,valueInt);
			break;
		case "price":
			if(tf_query.getText().equals("")) {
				tf_query.setText("0");
			}
			valueDouble = new Double(tf_query.getText()).doubleValue();
			list = BookDao.selectBookList(field,valueDouble);
			break;
		}
		addRowToModel(list);
	}
	
	/**
	 * 调试
	 * @param args
	 */
	//public static void main(String[] args) {
		//new BookQuery();
	//}

}
