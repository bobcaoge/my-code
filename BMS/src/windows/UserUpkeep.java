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
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��25������1:33:29
 * @copyright СȺ����ô��ô��Ů��
 * @aim  �û�ά����������
 */
public class UserUpkeep extends PublicJFrame{
	
	private JTextField tf_id;
	private JTextField tf_name;
	private JPasswordField pf_pass;
	private JComboBox<String>jc_isAdmin;
	
	private JButton jb_insert,jb_update,jb_cancel,jb_close,jb_delete,jb_empty;
	private JTable table;
	
	private DefaultTableModel model = new DefaultTableModel(new Object[][] {},
			new String[] {"���","����","����","����ԱȨ��"});
	
	private List<User>list = UserDao.selectUserList();
	
	UserUpkeep(){
		this.setTitle("--�û���Ϣά��--");
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
				"�û���Ϣά��",TitledBorder.LEADING,TitledBorder.TOP,
				new Font("΢���ź�", Font.PLAIN, 14),new Color(59, 59, 59)));
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
	 * �����������
	 * @return
	 */
	private JPanel createDataPal() {
		JPanel dataPanel = new JPanel(null);
		dataPanel.setBorder(new EmptyBorder(5, 5, 5, 10));
		dataPanel.setOpaque(false);
		JLabel jl_id = new JLabel("��ţ�");
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
		tf_id.setToolTipText("���������û����");
		dataPanel.add(tf_id);
		JLabel jl_name = new JLabel("�û�����");
		jl_name.setBounds(50,60,100,25);
		dataPanel.add(jl_name);
		tf_name = new JTextField(10);
		tf_name.setBounds(130,60,150,25);
		tf_name.setToolTipText("���������û���");
		dataPanel.add(tf_name);
		tf_name.addFocusListener(new FocusAdapter() {
			public void focusLost(FocusEvent e) {
				tf_name_focusLost();
			}	
		});
		
		JLabel jl_pass1 = new JLabel("���룺");
		jl_pass1.setBounds(50,100,100,25);
		dataPanel.add(jl_pass1);
		pf_pass = new JPasswordField(10);
		pf_pass.setBounds(130,100,150,25);
		pf_pass.setToolTipText("���������û�����");
		dataPanel.add(pf_pass);
		
		JLabel jl_isAdmin = new JLabel("����Ȩ�ޣ�");
		jl_isAdmin.setBounds(50,140,100,25);
		dataPanel.add(jl_isAdmin);
		
		String[] admin = new String[] {"����Ա", "����Ա", "һ���û�"};
		jc_isAdmin = new JComboBox<String>(admin);
		jc_isAdmin.setBounds(130,140,150,25);
		dataPanel.add(jc_isAdmin);
		
		return dataPanel;
		
	}
	
	/**
	 * ���� ��ť���
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
		
		jb_insert = new JButton("���");
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
		jb_update = new JButton("�޸�");
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
		jb_delete = new JButton("ɾ��");
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
		jb_cancel = new JButton("ȡ��");
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
		jb_close = new JButton("�ر�");
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
		jb_empty = new JButton("�����������");
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
	 * ����������
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
	 * ��굥���¼���Ӧ����
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
		int m = JOptionPane.showConfirmDialog(null, "ȷ��Ҫɾ��ȫ���û���", "����û�", JOptionPane.YES_NO_OPTION);
		if(m == JOptionPane.YES_NO_OPTION) {
			int n =JOptionPane.showConfirmDialog(null, "ȷ��Ҫ��������û���", "��������ٴ�ȷ��", JOptionPane.YES_NO_OPTION);
			if(n == JOptionPane.YES_NO_OPTION) {
				UserDao.emptyUser();
				refresh();
				del_content();
			}
		}
	}

	/**
	 * ���  ������� �е�����
	 */
	public void del_content() {
		// TODO Auto-generated method stub
		tf_id.setText(String.valueOf(list.size() + 1));
		tf_name.setText("");
		pf_pass.setText("");
		jc_isAdmin.setSelectedItem("����Ա");
		tf_id.setEditable(true);
		
	}


	/**
	 * ɾ���û�
	 */
	public void jb_delete_actionPerformed() {
		// TODO Auto-generated method stub
		int id = Integer.parseInt(tf_id.getText());
		int m  = JOptionPane.showConfirmDialog(null, "ȷ��Ҫɾ�������û���Ϣ��", "ɾ���û���Ϣ", JOptionPane.YES_NO_OPTION);
		if(m == JOptionPane.YES_OPTION) {
			if(UserDao.deleteUser(id) == 1) {
				refresh();
				JOptionPane.showMessageDialog(null, "ɾ���û���Ϣ�ɹ�");
			}

		}
		del_content();
	}

	/**
	 * �޸��û���Ϣ
	 */
	public void jb_update_actionPerformed() {
		// TODO Auto-generated method stub
		User user = new User();
		user.setId(Integer.parseInt(tf_id.getText().trim()));
		user.setName(tf_name.getText().trim());
		user.setPass(new String(pf_pass.getPassword()).trim());
		int is_admin = 2;
		if(jc_isAdmin.getSelectedItem().toString().equals("����Ա")) {
			is_admin = 1;
		}else {
			if(jc_isAdmin.getSelectedItem().toString().equals("����Ա")) {
				is_admin = 0;
			}
		}
		user.setIs_admin((byte)is_admin);
		if(tf_name.getText().trim().equals("")
				|| new String(pf_pass.getPassword()).trim().equals("")) {
			JOptionPane.showMessageDialog(null, "�û���Ϣ����Ϊ��");
			return;
		}else {
			int i = UserDao.updateUser(user);
			if(i == 1) {
				JOptionPane.showMessageDialog(null, "�޸��û���Ϣ�ɹ���");
			}
			refresh();
			del_content();
		}
	}

	/**
	 * ������û�
	 */
	public void jb_insert_actionPerformed() {
		// TODO Auto-generated method stub
		User user = new User();
		user.setId(Integer.parseInt(tf_id.getText().trim()));
		user.setName(tf_name.getText().trim());
		user.setPass(new String(pf_pass.getPassword()).trim());
		int is_admin = 2;
		if(jc_isAdmin.getSelectedItem().toString().equals("����Ա")) {
			is_admin = 1;
		}else {
			if(jc_isAdmin.getSelectedItem().toString().equals("����Ա")) {
				is_admin = 0;
			}
		}
		user.setIs_admin((byte)is_admin);
		
		if(tf_name.getText().trim().equals("")
				|| new String(pf_pass.getPassword()).trim().equals("")) {
			JOptionPane.showMessageDialog(null, "�û���Ϣ����Ϊ��");
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
	 * ����ı���ʧȥ�����¼���Ӧ����
	 */
	public void tf_id_focusLost() {
		// TODO Auto-generated method stub
		User user = UserDao.getUser(Integer.parseInt(tf_id.getText().trim()));
		if(user != null) {
			JOptionPane.showMessageDialog(null, "�û�����Ѵ��ڣ������������û���ţ�");
			del_content();
		}
		
	}
	
	/**
	 * �û����ı���ʧȥ�����¼�����Ӧ����
	 */
	public void tf_name_focusLost() {
		// TODO Auto-generated method stub
		User user = UserDao.getUser(tf_name.getText().trim());
		if(user != null) {
			JOptionPane.showMessageDialog(null, "�û����Ѵ��ڣ������������û���");
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
	
	//���Է���
	//public static void main(String args[]) {
	//	new UserUpkeep();
	//}


}
