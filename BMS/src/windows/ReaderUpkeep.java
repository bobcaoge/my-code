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

import data.ReaderDao;
import entity.Reader;
import util.Constant;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月25日下午9:57:38
 * @copyright 小群子怎么那么淑女呢
 * @aim  读者维护
 */
public class ReaderUpkeep extends PublicJFrame{
	
	private JTextField tf_id;
	private JTextField tf_name;
	private JComboBox<String>cb_type;
	private JComboBox<String>cb_sex;
	private JTextField tf_max_num;
	private JTextField tf_days_num;
	
	private JButton jb_insert,jb_update,jb_cancel,jb_close,jb_delete,jb_empty;
	private JTable table;
	private DefaultTableModel model = new DefaultTableModel(
			new Object[][] {}, new String[] {
					"编号","姓名","读者类型","性别","最大借书数量","最多借书天数"
			});
	
	private List<Reader>list = ReaderDao.selectReaderList();
	
	ReaderUpkeep(){
		this.setTitle("--读者信息维护--");
		setBounds(220,100,1000,500);
		this.setResizable(true);
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
				"读者信息维护",TitledBorder.LEADING,TitledBorder.TOP,
				new Font("微软雅黑", Font.PLAIN, 14),
				new Color(59, 59, 59)));
		innerPane.setResizeWeight(0.8);
		innerPane.setOrientation(JSplitPane.VERTICAL_SPLIT);
		outerPane.setLeftComponent(innerPane);
		JPanel dataPanel = createDataPanel();
		innerPane.setLeftComponent(dataPanel);
		JPanel buttonPanel = createButtonPanel();
		innerPane.setRightComponent(buttonPanel);
		JPanel tablePanel  = createTablePanel();
		outerPane.setRightComponent(tablePanel);
	}
	
	/**
	 * 表格面板
	 * @return
	 */
	private JPanel createTablePanel() {
		// TODO Auto-generated method stub
		JPanel tablePanel = new JPanel(new BorderLayout(5, 5));
				JScrollPane scrollPane = new JScrollPane();
		tablePanel.add(scrollPane);
		table = new JTable(model);
		
		for (int i = 0; i < list.size(); i++) {
			Reader reader = (Reader)list.get(i);
			model.addRow(new Object[] {reader.getId(),
					reader.getName(),reader.getType(),
					reader.getSex(),reader.getMax_num(),
					reader.getDays_num()
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
	 * 表格鼠标响应
	 */
	public void table_mouseClicked() {
		// TODO Auto-generated method stub
		Reader reader_old = (Reader)list.get(table.getSelectedRow());
		tf_id.setText(reader_old.getId());
		tf_name.setText(reader_old.getName());
		cb_type.setSelectedItem(reader_old.getType());
		cb_sex.setSelectedItem(reader_old.getSex());
		tf_max_num.setText(String.valueOf(reader_old.getMax_num()));
		tf_days_num.setText(String.valueOf(reader_old.getDays_num()));
		tf_id.setEditable(false);
		
	}

	/**
	 * @return数据面板
	 */
	private JPanel createDataPanel() {
		// TODO Auto-generated method stub
		JPanel dataPanel = new JPanel(null);
		dataPanel.setBorder(new EmptyBorder(5, 5, 5, 10));
		dataPanel.setOpaque(false);
		
		JLabel jl_id = new JLabel("编号：");
		jl_id.setBounds(50, 20, 100, 25);
		dataPanel.add(jl_id);
		
		tf_id = new JTextField();
		tf_id.setBounds(160, 20, 150, 25);
		
		tf_id.setToolTipText("必须输入读者编号");
		tf_id.addFocusListener(new FocusAdapter() {
			public void focusLost(FocusEvent e) {
				tf_id_fousLost();
			}
		});
		dataPanel.add(tf_id);
		
		JLabel jl_name = new JLabel("读者名称：");
		jl_name.setBounds(50, 60, 100, 25);
		dataPanel.add(jl_name);
		
		tf_name = new JTextField(10);
		tf_name.setBounds(160, 60, 150, 25);
		tf_name.setToolTipText("必须输入读者名");
		dataPanel.add(tf_name);
		
		JLabel jl_type  = new JLabel("读者类型：");
		jl_type.setBounds(50, 100, 150, 25);
		dataPanel.add(jl_type);
		
		cb_type = new JComboBox<String>(Constant.READER_TYPES);
		cb_type.setBounds(160, 100, 150, 25);
		dataPanel.add(cb_type);
		
		JLabel jl_sex = new JLabel("性别：");
		jl_sex.setBounds(50, 140, 150, 25);
		dataPanel.add(jl_sex);
		
		cb_sex = new JComboBox<String>(Constant.SEX);
		cb_sex.setBounds(160, 140, 150, 25);
		dataPanel.add(cb_sex);
		
		JLabel jl_max_num = new JLabel("最大借书量：");
		jl_max_num.setBounds(50, 180, 150, 25);
		dataPanel.add(jl_max_num);
		
		tf_max_num = new JTextField(10);
		tf_max_num.setBounds(160, 180, 150, 25);
		dataPanel.add(tf_max_num);
		
		JLabel jl_days_num = new JLabel("最大借书天数：");
		jl_days_num.setBounds(50, 220, 150, 25);
		dataPanel.add(jl_days_num);
		
		tf_days_num = new JTextField(10);
		tf_days_num.setBounds(160, 220, 150, 25);
		dataPanel.add(tf_days_num);
		
		return dataPanel;
	}
	
	/**
	 * 读者编号文本框 事件响应方法
	 */
	public void tf_id_fousLost() {
		// TODO Auto-generated method stub
		Reader reader = ReaderDao.getReaderById(tf_id.getText().trim());
		if(reader != null) {
			JOptionPane.showMessageDialog(null, "已存在，请重新输入读者编号！");
			del_content();
		}
	}

	/**
	 * 按钮面板
	 * @return
	 */
	private JPanel createButtonPanel() {
		JPanel buttonPanel = new JPanel(new GridBagLayout());
		buttonPanel.setOpaque(false);
		((GridBagLayout)buttonPanel.getLayout()).columnWidths = new int[] {
				0,60,60,60,60,60,0
		};
		((GridBagLayout)buttonPanel.getLayout()).columnWeights = new double[] {
				0.5,0.0,0.0,0.0,0.0,0.0,0.5
		};
		jb_insert = new JButton("添加");
		jb_insert.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				jb_insert_actionPerformed();
			}
		});
		buttonPanel.add(jb_insert, new GridBagConstraints(1,0,1,1,0.0,0.0,
				GridBagConstraints.CENTER,
				GridBagConstraints.BOTH,
				new Insets(0, 0, 0, 5),0,0));
		
		jb_update = new JButton("修改");
		jb_update.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				jb_update_actionPerformed();
			}
		});
		
		buttonPanel.add(jb_update,
				new GridBagConstraints(2,0,1,1,0.0,0.0,
						GridBagConstraints.CENTER,
						GridBagConstraints.BOTH,
						new Insets(0, 0, 0, 5),0,0));
		
		jb_delete = new JButton("删除");
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
		
		jb_cancel = new JButton("取消");
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
		
		jb_close = new JButton("关闭");
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
		
		jb_empty = new JButton("清空所有读者");
		
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
	 * 删除所有读者信息
	 */
	protected void jb_empty_actionPerformed() {
		// TODO Auto-generated method stub
		int m = JOptionPane.showConfirmDialog(null, "删除所有读者信息？","清空读者信息",JOptionPane.YES_NO_CANCEL_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			int n = JOptionPane.showConfirmDialog(null, "确定要清除所有读者信息？","再次确认清除所有信息？",JOptionPane.YES_NO_OPTION);
			if(n == JOptionPane.YES_OPTION) {
				ReaderDao.emptyReader();
				refresh();
				del_content();
			}
		}
		
	}

	/**
	 * 清空数据面板
	 */
	public void del_content() {
		// TODO Auto-generated method stub
		tf_id.setText("");
		tf_id.setEditable(true);
		tf_name.setText("");
		cb_type.setSelectedIndex(0);
		cb_sex.setSelectedItem("管理员");
		tf_max_num.setText("");
		tf_days_num.setText("");
	}

	/**
	 * 删除读者信息
	 */
	public void jb_delete_actionPerformed() {
		// TODO Auto-generated method stub
		String id = tf_id.getText().trim();
		int m = JOptionPane.showConfirmDialog(null, "确认要删除吗？","删除读者信息",JOptionPane.YES_NO_CANCEL_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			if(ReaderDao.deleteReader(id) == 1) {
				refresh();
				JOptionPane.showMessageDialog(null, "删除成功！");
			}
			del_content();
		}
	}

	/**
	 * 修改读者信息
	 */
	public void jb_update_actionPerformed() {
		// TODO Auto-generated method stub
		Reader reader = new Reader();
		reader.setId(tf_id.getText().trim());
		reader.setName(tf_name.getText().trim());
		reader.setType(cb_type.getSelectedItem().toString());
		reader.setSex(cb_sex.getSelectedItem().toString());
		reader.setMax_num(new Integer(tf_max_num.getText().trim()));
		reader.setDays_num(new Integer(tf_days_num.getText().trim()));
		if(tf_name.getText().trim().equals("") || tf_id.getText().trim().equals("")) {
			JOptionPane.showMessageDialog(null, "读者信息不能为空");
			return;
		}else {
			int i = ReaderDao.updateReader(reader);
			if(i == 1) {
				JOptionPane.showMessageDialog(null, "修改成功！");
			}
			refresh();
			del_content();
		}
	}

	/**
	 * 添加读者
	 */
	public void jb_insert_actionPerformed() {
		// TODO Auto-generated method stub
		Reader reader = new Reader();
		reader.setId(tf_id.getText().trim());
		reader.setName(tf_name.getText().trim());
		reader.setType(cb_type.getSelectedItem().toString());
		reader.setSex(cb_sex.getSelectedItem().toString());
		reader.setMax_num(new Integer(tf_max_num.getText().trim()));
		reader.setDays_num(new Integer(tf_days_num.getText().trim()));
		
		if(tf_name.getText().trim().equals("") || tf_id.getText().trim().equals("")) {
			JOptionPane.showMessageDialog(null, "读者信息不能为空");
			return;
		}else {
			int i = ReaderDao.insertReader(reader);
			if(i == 1) {
				model.addRow(new Object[] {
						reader.getId(),reader.getName(),reader.getType(),
						reader.getSex(),reader.getMax_num(),
						reader.getDays_num()
				});
				refresh();
			}
			del_content();
		}
	}
	
	/**
	 * 更新数据表格
	 */
	public void refresh() {
		model.setRowCount(0);
		list = ReaderDao.selectReaderList();
		for(int i = 0;i < list.size();i++) {
			Reader reader = (Reader)list.get(i);
			model.addRow(new Object[] {
					reader.getId(),reader.getName(),reader.getType(),
					reader.getSex(),reader.getMax_num(),
					reader.getDays_num()
			});
		}
		del_content();
	}
	
	/**
	 * 测试
	 * @param args
	 */
	//public static void main(String args[]) {
	//	new ReaderUpkeep();
	//}
}
