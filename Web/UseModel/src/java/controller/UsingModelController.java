/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Lenovo
 */
@WebServlet(name = "UsingModelController", urlPatterns = {"/UsingModelController"})
public class UsingModelController extends HttpServlet {
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try{
            String language = request.getParameter("language");
            String pythonPath = "C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe";
            String scriptPath = "C:/Users/Lenovo/PycharmProjects/modelCreation/Main.py";
            String[] command = {pythonPath, scriptPath, language};
            ProcessBuilder processBuilder = new ProcessBuilder(command);

            // Rediriger la sortie du processus pour la lire
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // Lire la sortie du processus
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            String res ="";

            while ((line = reader.readLine()) != null) {
                res += line;
            }
            
            String[] results = res.split(",");
            
            String modeleResult = results[0];
            
            String sardinas = "";
            if(results[1].contains("True"))sardinas="Language is decodable";
                    else sardinas="Language is not decodable";
            
            String sardinasResult = sardinas;
            
            request.setAttribute("language",language);
            request.setAttribute("modeleResult", modeleResult);
            request.setAttribute("sardinasResult", sardinasResult);           
            
            RequestDispatcher dispatcher = request.getRequestDispatcher("response.jsp");
            dispatcher.forward(request,response);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }
    
    
    @Override
    public String getServletInfo() {
        return "Short description";
    }

}
