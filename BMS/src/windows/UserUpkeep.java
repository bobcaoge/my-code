/**
 * 
 */
package windows;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
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
import javax.swing.JPasswordField;
import javax.swing.JScrollBar;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.border.EtchedBorder;
import javax.swing.border.TitledBorder;
import javax.swing.table.DefaultTableModel;

import data.UserDao;
import entity.User;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月25日下午1:33:29
 * @copyright 小群子怎么那么淑女呢
 * @aim  用户维护操作界面
 */
public class UserUpkeep extends PublicJFrame{
	
	private JTextField tf_id;
	private JTextField tf_name;
	private JPasswordField pf_pass;
	private JComboBox<String>jc_isAdmin;
	
	private JButton jb_insert,jb_update,jb_cancel,jb_close,jb_delete,jb_empty;
	private JTable table;
	
	private DefaultTableModel model = new DefaultTableModel(new Object[][] {},
			new String[] {"编号","姓名","密码","管理员权限"});
	
	private List<User>list = UserDao.selectUserList();
	
	UserUpkeep(){
		this.setTitle("--用户信息维护--");
		setBounds(220,100,800,400);
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
		innerPane.setBorder(new TitledBorder(new EtchedBorder(EtchedBorder.LOWERED,null,null),
				"用户信息维护",TitledBorder.LEADING,TitledBorder.TOP,
				new Font("微软雅黑", Font.PLAIN, 14),new Color(59, 59, 59)));
		innerPane.setResizeWeight(0.8);
		innerPane.setOrientation(JSplitPane.VERTICAL_SPLIT);
		outerPane.setLeftComponent(innerPane);
		innerPane.setLeftComponent(createDataPal());
		innerPane.setRightComponent(createButtonPanel());
		outerPane.setRightComponent(createTablePanel());
		
	}
	
	/**
	 * @return
	 */

	
	/**
	 * 创建数据面板
	 * @return
	 */
	private JPanel createDataPal() {
		JPanel dataPanel = new JPanel(null);
		dataPanel.setBorder(new EmptyBorder(5, 5, 5, 10));
		dataPanel.setOpaque(false);
		JLabel jl_id = new JLabel("编号：");
		jl_id.setBounds(50,20,100,25);
		dataPanel.add(jl_id);
		if(list.size() == 0) {
			tf_id = new JTextField(String.valueOf(1));
		}else {
			tf_id = new JTextField(String.valueOf(list.size() + 1));
		}
		tf_id.addFocusListener(new FocusAdapter() {
			public void focusLost(FocusEvent e) {
				tf_id_focusLost();
			}
		});
		tf_id.setBounds(130,20,150,25);
		tf_id.setToolTipText("必须输入用户编号");
		dataPanel.add(tf_id);
		JLabel jl_name = new JLabel("用户名：");
		jl_name.setBounds(50,60,100,25);
		dataPanel.add(jl_name);
		tf_name = new JTextField(10);
		tf_name.setBounds(130,60,150,25);
		tf_name.setToolTipText("必须输入用户名");
		dataPanel.add(tf_name);
		tf_name.addFocusListener(new FocusAdapter() {
			public void focusLost(FocusEvent e) {
				tf_name_focusLost();
			}	
		});
		
		JLabel jl_pass1 = new JLabel("密码：");
		jl_pass1.setBounds(50,100,100,25);
		dataPanel.add(jl_pass1);
		pf_pass = new JPasswordField(10);
		pf_pass.setBounds(130,100,150,25);
		pf_pass.setToolTipText("必须输入用户密码");
		dataPanel.add(pf_pass);
		
		JLabel jl_isAdmin = new JLabel("管理权限：");
		jl_isAdmin.setBounds(50,140,100,25);
		dataPanel.add(jl_isAdmin);
		
		String[] admin = new String[] {"管理员", "操作员", "一般用户"};
		jc_isAdmin = new JComboBox<String>(admin);
		jc_isAdmin.setBounds(130,140,150,25);
		dataPanel.add(jc_isAdmin);
		
		return dataPanel;
		
	}
	
	/**
	 * 创建 按钮面板
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
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_insert_actionPerformed();
			}
		});
		buttonPanel.add(jb_insert,
				new GridBagConstraints(1,0,1,1,0.0,0.0,GridBagConstraints.CENTER,
				GridBagConstraints.BOTH,new Insets(0, 0, 0, 5),0,0));
		jb_update = new JButton("修改");
		jb_update.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_update_actionPerformed();
			}
		});
		buttonPanel.add(jb_update,
				new GridBagConstraints(2, 0, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER,
						GridBagConstraints.BOTH, new Insets(0, 0, 0, 5), 0, 0));
		jb_delete = new JButton("删除");
		jb_delete.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_delete_actionPerformed();
			}
		});
		buttonPanel.add(jb_delete,
				new GridBagConstraints(3, 0, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER,
						GridBagConstraints.BOTH, new Insets(0, 0, 0, 5), 0, 0));
		jb_cancel = new JButton("取消");
		jb_cancel.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				del_content();
			}
		});
		buttonPanel.add(jb_cancel,
				new GridBagConstraints(4, 0, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER,
						GridBagConstraints.BOTH, new Insets(0, 0, 0, 5), 0, 0));
		jb_close = new JButton("关闭");
		jb_close.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
			}
		});
		buttonPanel.add(jb_close,
				new GridBagConstraints(5, 0, 1, 1, 0.0, 0.0, GridBagConstraints.CENTER,
						GridBagConstraints.BOTH, new Insets(0, 0, 0, 5), 0, 0));
		jb_empty = new JButton("清空所有数据");
		jb_empty.setBounds(160, 280, 160, 25);
		jb_empty.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				jb_empty_actionPerformed();
			}
		});
		buttonPanel.add(jb_empty,
				new GridBagConstraints(2, 1, 3, 1, 0.0, 0.0, GridBagConstraints.CENTER,
						GridBagConstraints.BOTH, new Insets(25, 0, 0, 0), 0, 0));
		return buttonPanel;
	}
	
	/**
	 * 创建表格面板
	 * @return
	 */
	private JPanel createTablePanel() {
		// TODO Auto-generated method stub
		JPanel tablePanel = new JPanel(new BorderLayout(5,5));
		JScrollPane scrollPane = new JScrollPane();
		tablePanel.add(scrollPane);
		table = new JTable(model);
		for (int i = 0; i < list.size(); i++) {
			User user = (User)list.get(i);
			model.addRow(new Object[] {user.getId(),user.getName(),user.getPass(),user.getIs_admin()});
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
	 * 鼠标单击事件响应方法
	 */
	public void table_mouseClicked() {
		// TODO Auto-generated method stub
		User user = (User)list.get(table.getSelectedRow());
		tf_id.setText(String.valueOf(user.getId()));
		tf_name.setText(user.getName());
		pf_pass.setText(user.getPass());
		if(user.getIs_admin() == 1) {
			jc_isAdmin.setSelectedIndex(1);
		}else {
			if(user.getIs_admin() == 0) {
				jc_isAdmin.setSelectedIndex(1);
			}else {
				jc_isAdmin.setSelectedIndex(2);
			}
		}
		tf_id.setEditable(false);
	}

	/**
	 * 
	 */
	public void jb_empty_actionPerformed() {
		// TODO Auto-generated method stub
		int m = JOptionPane.showConfirmDialog(null, "确认要删除全部用户吗？", "清空用户", JOptionPane.YES_NO_OPTION);
		if(m == JOptionPane.YES_NO_OPTION) {
			int n =JOptionPane.showConfirmDialog(null, "确认要清空所有用户吗？", "清空用于再次确认", JOptionPane.YES_NO_OPTION);
			if(n == JOptionPane.YES_NO_OPTION) {
				UserDao.emptyUser();
				refresh();
				del_content();
			}
		}
	}

	/**
	 * 清空  数据面板 中的数据
	 */
	public void del_content() {
		// TODO Auto-generated method stub
		tf_id.setText(String.valueOf(list.size() + 1));
		tf_name.setText("");
		pf_pass.setText("");
		jc_isAdmin.setSelectedItem("管理员");
		tf_id.setEditable(true);
		
	}


	/**
	 * 删除用户
	 */
	public void jb_delete_actionPerformed() {
		// TODO Auto-generated method stub
		int id = Integer.parseInt(tf_id.getText());
		int m  = JOptionPane.showConfirmDialog(null, "确认要删除这条用户信息吗？", "删除用户信息", JOptionPane.YES_NO_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			if(UserDao.deleteUser(id) == 1) {
				refresh();
				JOptionPane.showMessageDialog(null, "删除用户信息成功");
			}

		}
		del_content();
	}

	/**
	 * 修改用户信息
	 */
	public void jb_update_actionPerformed() {
		// TODO Auto-generated method stub
		User user = new User();
		user.setId(Integer.parseInt(tf_id.getText().trim()));
		user.setName(tf_name.getText().trim());
		user.setPass(new String(pf_pass.getPassword()).trim());
		int is_admin = 2;
		if(jc_isAdmin.getSelectedItem().toString().equals("管理员")) {
			is_admin = 1;
		}else {
			if(jc_isAdmin.getSelectedItem().toString().equals("操作员")) {
				is_admin = 0;
			}
		}
		user.setIs_admin((byte)is_admin);
		if(tf_name.getText().trim().equals("")
				|| new String(pf_pass.getPassword()).trim().equals("")) {
			JOptionPane.showMessageDialog(null, "用户信息不能为空");
			return;
		}else {
			int i = UserDao.updateUser(user);
			if(i == 1) {
				JOptionPane.showMessageDialog(null, "修改用户信息成功！");
			}
			refresh();
			del_content();
		}
	}

	/**
	 * 添加新用户
	 */
	public void jb_insert_actionPerformed() {
		// TODO Auto-generated method stub
		User user = new User();
		user.setId(Integer.parseInt(tf_id.getText().trim()));
		user.setName(tf_name.getText().trim());
		user.setPass(new String(pf_pass.getPassword()).trim());
		int is_admin = 2;
		if(jc_isAdmin.getSelectedItem().toString().equals("管理员")) {
			is_admin = 1;
		}else {
			if(jc_isAdmin.getSelectedItem().toString().equals("操作员")) {
				is_admin = 0;
			}
		}
		user.setIs_admin((byte)is_admin);
		
		if(tf_name.getText().trim().equals("")
				|| new String(pf_pass.getPassword()).trim().equals("")) {
			JOptionPane.showMessageDialog(null, "用户信息不能为空");
			return;
		}else {
			int i = UserDao.insertUser(user);
			if( i == 1) {
				model.addRow(new Object[] {
					user.getId(),user.getName(),user.getPass(),user.getIs_admin()
				});
				refresh();
			}
			del_content();
		}
	}

	/**
	 * 编号文本框失去焦点事件响应方法
	 */
	public void tf_id_focusLost() {
		// TODO Auto-generated method stub
		User user = UserDao.getUser(Integer.parseInt(tf_id.getText().trim()));
		if(user != null) {
			JOptionPane.showMessageDialog(null, "用户编号已存在，请重新输入用户编号！");
			del_content();
		}
		
	}
	
	/**
	 * 用户名文本框失去焦点事件的响应方法
	 */
	public void tf_name_focusLost() {
		// TODO Auto-generated method stub
		User user = UserDao.getUser(tf_name.getText().trim());
		if(user != null) {
			JOptionPane.showMessageDialog(null, "用户名已存在，请重新输入用户名");
			tf_name.setText("");
		}
	}
	
	
	public void refresh() {
		model.setRowCount(0);
		list = UserDao.selectUserList();
		for (int i = 0; i < list.size(); i++) {
			User user = (User)list.get(i);
			model.addRow(new Object[] {user.getId(),user.getName(),user.getPass(),user.getIs_admin()});
		}
		del_content();
	}
	
	//测试方法
	//public static void main(String args[]) {
	//	new UserUpkeep();
	//}


}
