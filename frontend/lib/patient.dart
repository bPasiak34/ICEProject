import 'package:flutter/material.dart';

class PatientPage extends StatefulWidget {
  const PatientPage({super.key});

  @override
  State<StatefulWidget> createState() => PatientPageState();
}

class PatientPageState extends State<PatientPage> {
  void moveTo(Widget next) {}

  PatientPageState();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Patient page"),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Center(
        child: GridView.count(
          crossAxisCount: 3,
          children: List.generate(6,
          (index) => Center(
                      child: ElevatedButton(
                        child: Text("Button $index"),
                        onPressed: () {},
                        )
                      )
          ),
        ),
      ),
    );
  }
}
