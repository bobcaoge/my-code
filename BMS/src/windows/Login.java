/**
 * 
 */
package windows;

import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

import data.UserDao;
import entity.User;
import util.GlobalVar;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��23������2:48:02
 * @copyright СȺ����ô��ô��Ů��
 * @aim
 */
public class Login extends PublicJFrame{
	private JTextField tf_user;          //�����û����ı���
	private JPasswordField pf_pass;      //���������
	private JButton bt_login;            //�����½��ť
	private JButton bt_close;            //����رհ�ť
	
	/**
	 * ���췽�� ���ڳ�ʼ�� ��½����
	 */
	Login(){
		this.getContentPane().setLayout(null);//��ȡ���������� �����������Ĳ���Ϊ���Բ���
		JLabel lb_user = new JLabel("�û�����");  //�����û�����ǩ
		lb_user.setBounds(new Rectangle(100, 50, 70, 25)); //�����û�����ǩ�ķ���λ�úͷ��ô�С
		add(lb_user);
		
		tf_user = new JTextField();
		tf_user.setBounds(new Rectangle(170, 50, 110, 25));
		add(tf_user);
		JLabel lb_pass = new JLabel("���룺");
		lb_pass.setBounds(new Rectangle(100, 90, 50, 25));
		add(lb_pass);
		
		pf_pass = new JPasswordField();
		pf_pass.setBounds(new Rectangle(170, 90, 110, 25));
		add(pf_pass);
		
		bt_login = new JButton("��½");
		bt_login.setBounds(new Rectangle(100, 160, 80, 25));
		bt_login.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				bt_login_actionPerformed();
			}
		});
		add(bt_login);
		
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
		setTitle("BMW_LABͼ�����ϵͳ--BY_Qun");
		setSize(380,260);
		setResizable(true);   //���õ�½�����С�ɱ�
		setLocationRelativeTo(null);  //���õ�½�����С����Ļ����
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //���ý��� Ĭ�Ϲرղ���
	}
	
	/**
	 * "��½"��ť��ʱ����Ӧ����
	 */
	void bt_login_actionPerformed() {
		String name = tf_user.getText().trim();
		String pass = new String(pf_pass.getPassword()).trim();
		if(name.equals("")||pass.equals("")) {
			JOptionPane.showMessageDialog(this,"�û���Ϣ������Ϊ�գ�");
			return;
		}
		User user = UserDao.getUser(name,pass);
		if(user != null) {
			GlobalVar.login_user = user;
			MainFrame main = new MainFrame();
			main.setPurView((byte)user.getIs_admin());
			this.dispose();
		}else {
			JOptionPane.showMessageDialog(this,"�û������������");
			tf_user.setText("");
			pf_pass.setText("");
			return;
		}
	}
	
	
	public static void main(String args[]) {
		new Login();   //������½����
	}
}
