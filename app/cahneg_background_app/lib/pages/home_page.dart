import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  
  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    double screenHeight = MediaQuery.of(context).size.height;
    return Scaffold(
      body: ListView(
        children: [
          Center(
            child: Container(
              width: screenWidth - 200, 
              height: screenHeight - 600,
              margin: EdgeInsets.only(top: screenHeight - 650),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                color: Colors.red, 
              ),
            ),
          )
        ],
      ),
    );
  }
}