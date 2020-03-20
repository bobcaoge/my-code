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

import data.ReaderDao;
import entity.Reader;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��27������1:47:51
 * @copyright СȺ����ô��ô��Ů��
 * @aim ���߲�ѯ
 */
public class ReaderQuery extends PublicJFrame{
	
	JLabel lb_query;
	JTextField tf_query;
	JComboBox<String>cb_query;
	JButton bt_query;
	
	private JTable table;
	
	private List<Reader>list = ReaderDao.selectReaderList();
	private String[] tb_heads = {
			"���߱��","��������","��������","�Ա�","�ɽ�����","�ɽ�����"
	};
	
	private String[] fields = {
			"id","name","type","sex","max_num","days_num"
	};
	private DefaultTableModel model = new DefaultTableModel(new Object[][] {}, tb_heads);
	
	private String field = "id";
	String valueStr = "";
	int valueInt =0;
	
	/**
	 * ���߲�ѯ �����ʼ��
	 */
	 ReaderQuery() {
		// TODO Auto-generated constructor stub
		this.setTitle("���߲�ѯ");
		this.setVisible(true);
		this.setSize(1000,500);
		this.setLocationRelativeTo(null);
		
		JPanel queryPanel = createQueryPanel();
		this.add(queryPanel,BorderLayout.NORTH);
		
		JPanel tablePanel = createTablePanel();
		this.add(tablePanel,BorderLayout.CENTER);
		
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
		addRowToModel(list);
		scrollPane.setViewportView(table);
		return tablePanel;
	}

	/**
	 * ��Ӷ����б�
	 * @param list2
	 */
	private void addRowToModel(List<Reader> list2) {
		// TODO Auto-generated method stub
		model.setRowCount(0);
		for (int i = 0; i < list.size(); i++) {
			Reader reader = (Reader)list.get(i);
			model.addRow(new Object[] {
					reader.getId(),reader.getName(),
					reader.getType(),reader.getSex(),
					reader.getMax_num(),reader.getDays_num()
			});
		}
	}

	/**
	 * ��ѯ���
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
		
		lb_query = new JLabel("��������߱��");
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
					query_actionPerformed();
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
			public void itemStateChanged(ItemEvent arg0) {
				// TODO Auto-generated method stub
				cb_query_itemStateChanged(arg0);
			}
		});
		
		queryPanel.add(cb_query,
				new GridBagConstraints(3,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10, 0, 10, 10),0,0));
		
		bt_query = new JButton("��ѯ");
		bt_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				query_actionPerformed();
			}
		});
		
		queryPanel.add(bt_query,
				new GridBagConstraints(4,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(10, 0, 10, 10),0,0));
		
		JButton bn_close = new JButton("�ر�");
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
	 * ��ѯ��Ͽ�
	 * @param arg0
	 */
	private void cb_query_itemStateChanged(ItemEvent arg0) {
		// TODO Auto-generated method stub
		if(arg0.getStateChange() == ItemEvent.SELECTED) {
			lb_query.setText("������" + (String)arg0.getItem() + "��");
			tf_query.setText("");
			for (int i = 0; i < tb_heads.length; i++) {
				if(arg0.getItem().equals(tb_heads[i])) {
					field = fields[i];
				}
			}
			list = ReaderDao.selectReaderList();
			addRowToModel(list);
			tf_query.requestFocus();
		}
	}

	/**
	 * 
	 */
	private void query_actionPerformed() {
		// TODO Auto-generated method stub
		switch(field) {
		case "id":
		case "name":
		case "type":
		case "sex":
			valueStr = tf_query.getText();
			list = ReaderDao.selectReaderList(field,valueStr);
			break;
		case "max_num":
		case "days_num":
			if(tf_query.getText().equals("")) {
				valueInt = 0;
			}else {
				valueInt = new Double(tf_query.getText()).intValue();
			}
			list = ReaderDao.selectReaderList(field,valueInt);
			break;
		}
		addRowToModel(list);
	}
	
	//public static void main(String args[]) {
	//	new ReaderQuery();
	//}
	

}
