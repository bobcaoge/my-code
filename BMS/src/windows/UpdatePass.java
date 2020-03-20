/**
 * 
 */
package windows;

import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;

import data.UserDao;
import util.GlobalVar;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��27������8:24:24
 * @copyright СȺ����ô��ô��Ů��
 * @aim
 */
public class UpdatePass extends PublicJFrame{
	
	private JPasswordField pf_pass1;
	private JPasswordField pf_pass2;
	private JButton bt_ok;
	private JButton bt_close;
	
	/**
	 * 
	 */
	UpdatePass() {
		// TODO Auto-generated constructor stub
		setTitle("--�����޸�--");
		setSize(380,260);
		setResizable(true);
		setLocationRelativeTo(null);
		this.getContentPane().setLayout(null);
		JLabel lb_pass1 = new JLabel("���������룺");
		lb_pass1.setBounds(new Rectangle(100, 50, 70, 25));
		add(lb_pass1);
		
		pf_pass1 = new JPasswordField();
		pf_pass1.setBounds(new Rectangle(180, 50, 110, 25));
		add(pf_pass1);
		
		JLabel lb_pass2 = new JLabel("ȷ�����룺");
		lb_pass2.setBounds(new Rectangle(100, 90, 70, 25));
		add(lb_pass2);
		
		pf_pass2 = new JPasswordField();
		pf_pass2.setBounds(new Rectangle(180, 90, 110, 25));
		add(pf_pass2);
		
		bt_ok = new JButton("�޸�");
		bt_ok.setBounds(new Rectangle(100, 160, 80, 25));
		
		bt_ok.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				ok_actionPerformed();
			}
		});
		add(bt_ok);
		
		bt_close = new JButton("�ر�");
		bt_close.setBounds(new Rectangle(200, 160, 80, 25));
		
		bt_close.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
			}
		});
		add(bt_close);
	}

	/**
	 * �޸İ�ť
	 */
	void ok_actionPerformed() {
		// TODO Auto-generated method stub
		String pass1 = new String(pf_pass1.getPassword());
		String pass2 = new String(pf_pass2.getPassword());
		
		if(pass1.equals("") || pass2.equals("")) {
			JOptionPane.showMessageDialog(this, "�������û�����Ϊ�գ�");
			pf_pass1.requestFocus();
			return;
		}
		
		if(!pass1.equals(pass2)) {
			JOptionPane.showMessageDialog(this, "��������벻һ�£����������룡");
			pf_pass1.setText("");
			pf_pass2.setText("");
			pf_pass1.requestFocus();
			return;
		}
		
		if(GlobalVar.login_user != null) {
			String name = GlobalVar.login_user.getName();
			int i = UserDao.updatePass(name, pass1);
			if(i == 1) {
				JOptionPane.showMessageDialog(null, "�����޸ĳɹ����������������µ�¼��");
				dispose();
			}
		}else {
			JOptionPane.showMessageDialog(null, "�û������ڣ������޸�ʧ��");
		}
	}
	
	//public static void main(String[] args) {
	//	new UpdatePass();
	//}

}
