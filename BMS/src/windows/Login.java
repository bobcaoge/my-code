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
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月23日下午2:48:02
 * @copyright 小群子怎么那么淑女呢
 * @aim
 */
public class Login extends PublicJFrame{
	private JTextField tf_user;          //定义用户名文本框
	private JPasswordField pf_pass;      //定义密码框
	private JButton bt_login;            //定义登陆按钮
	private JButton bt_close;            //定义关闭按钮
	
	/**
	 * 构造方法 用于初始化 登陆界面
	 */
	Login(){
		this.getContentPane().setLayout(null);//获取框架内容面板 设置内容面板的布局为绝对布局
		JLabel lb_user = new JLabel("用户名：");  //创建用户名标签
		lb_user.setBounds(new Rectangle(100, 50, 70, 25)); //设置用户名标签的放置位置和放置大小
		add(lb_user);
		
		tf_user = new JTextField();
		tf_user.setBounds(new Rectangle(170, 50, 110, 25));
		add(tf_user);
		JLabel lb_pass = new JLabel("密码：");
		lb_pass.setBounds(new Rectangle(100, 90, 50, 25));
		add(lb_pass);
		
		pf_pass = new JPasswordField();
		pf_pass.setBounds(new Rectangle(170, 90, 110, 25));
		add(pf_pass);
		
		bt_login = new JButton("登陆");
		bt_login.setBounds(new Rectangle(100, 160, 80, 25));
		bt_login.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				bt_login_actionPerformed();
			}
		});
		add(bt_login);
		
		bt_close = new JButton("关闭");
		bt_close.setBounds(new Rectangle(200, 160, 80, 25));
		bt_close.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
				
			}
		});
		
		add(bt_close);
		setTitle("BMW_LAB图书管理系统--BY_Qun");
		setSize(380,260);
		setResizable(true);   //设置登陆界面大小可变
		setLocationRelativeTo(null);  //设置登陆界面大小在屏幕中央
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //设置界面 默认关闭操作
	}
	
	/**
	 * "登陆"按钮的时间响应方法
	 */
	void bt_login_actionPerformed() {
		String name = tf_user.getText().trim();
		String pass = new String(pf_pass.getPassword()).trim();
		if(name.equals("")||pass.equals("")) {
			JOptionPane.showMessageDialog(this,"用户信息不允许为空！");
			return;
		}
		User user = UserDao.getUser(name,pass);
		if(user != null) {
			GlobalVar.login_user = user;
			MainFrame main = new MainFrame();
			main.setPurView((byte)user.getIs_admin());
			this.dispose();
		}else {
			JOptionPane.showMessageDialog(this,"用户名或密码错误！");
			tf_user.setText("");
			pf_pass.setText("");
			return;
		}
	}
	
	
	public static void main(String args[]) {
		new Login();   //创建登陆界面
	}
}
