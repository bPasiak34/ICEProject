import 'package:flutter/material.dart';

import "patient.dart";
import "doctor.dart";

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ICE Project',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color.fromARGB(255, 23, 84, 124),
        ),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'App Name'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  void selectPatient() {
    Navigator.push(context, MaterialPageRoute(builder: (context) => const PatientPage()));
  }

  void selectDoctor() {
    Navigator.push(context, MaterialPageRoute(builder: (context) => const DoctorPage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            ElevatedButton(
              onPressed: selectPatient,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.fromLTRB(30, 20, 30, 20)
              ),
              child: Text(
                "I am a patient",
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.displaySmall
              ),
            ),
            Container(
              height: 30,
            ),
            ElevatedButton(
              onPressed: selectDoctor,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.fromLTRB(20, 10, 20, 10)
              ),
              child: Text(
                "I am a doctor",
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headlineSmall,
              )
            ),
          ],
        ),
      ),
    );
  }
}
