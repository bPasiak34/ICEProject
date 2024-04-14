import 'package:flutter/material.dart';

PageStorageKey doctorKey = const PageStorageKey("doctor");
final PageStorageBucket doctorBucket = PageStorageBucket();

class DoctorPage extends StatefulWidget {
  const DoctorPage({super.key});

  @override
  State<StatefulWidget> createState() => DoctorPageState();
}

class DoctorPageState extends State<DoctorPage> {
  final TextEditingController _codeController = TextEditingController();

  void submit(String code) {
    // verify if the code is valid
    code.replaceAll(RegExp(r"\s"), "");
    try {
      int.parse(code);
    } on FormatException catch (_) {
      showErrorDialog("Invalid code");
      return;
    }

    if (code.length != 6) {
      showErrorDialog("Invalid code");
      return;
    }
    doctorBucket.writeState(context, code, identifier: ValueKey(doctorKey));
    Navigator.push(
        context, MaterialPageRoute(builder: (context) => const DoctorOverview()));
  }

  void showErrorDialog(String msg) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("Error"),
          content: Text(msg),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: const Text("OK")
            )
          ],
        );
      }
    );
  }

  @override
  Widget build(BuildContext context) {
    return PageStorage(
      key: doctorKey,
      bucket: doctorBucket,
      child: Scaffold(
        appBar: AppBar(
          title: const Text("Doctor page"),
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Container(
                padding: const EdgeInsets.fromLTRB(50, 0, 50, 0),
                child: TextField(
                  keyboardType: TextInputType.number,
                  onSubmitted: submit,
                  controller: _codeController,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(), hintText: "Enter the patient code"
                  )
                ),
              ),
              ElevatedButton(
                onPressed: () {
                  submit(_codeController.text);
                },
                child: const Text("Submit")
              )
            ],
          )
        ),
      ),
    );
  }
} // bracket hell :/

class DoctorOverview extends StatefulWidget {
  const DoctorOverview({super.key});

  @override
  State<DoctorOverview> createState() => DoctorOverviewState();
}

class DoctorOverviewState extends State<DoctorOverview> {
  @override
  Widget build(BuildContext context) {
    String code = "invalid";
    if (doctorBucket.readState(context, identifier: ValueKey(doctorKey)) != null) {
      code = doctorBucket.readState(context, identifier: ValueKey(doctorKey));
    }

    return PageStorage(
      key: doctorKey,
      bucket: doctorBucket,
      child: Scaffold(
        appBar: AppBar(
          title: const Text("Doctor overview"),
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text("Your code is:"),
            Text(
              code,
              style: Theme.of(context).textTheme.headlineLarge,
            )
          ],
        ),
      )
    );
  }
} 
// y'know, i really don't know what am i doing in the frontend team
// well, no one else is gonna do it in this team, so i might as well try my best, eh?